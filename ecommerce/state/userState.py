import reflex as rx
from ecommerce import const
from ecommerce.dal.models.user import User
from ecommerce.dal.models.user import Address
from ecommerce.dal.dao.UserDAO import UserDAO
from ecommerce.dal.dao.AddressDAO import AddressDAO
import dotenv
from ecommerce.api import api
from ecommerce.routes import Route
from reflex_google_auth import GoogleAuthState, require_google_login
from fastapi import HTTPException, status


dotenv.load_dotenv()


# Class that manages the login pop-up
class LoginState(GoogleAuthState):
    show: bool = False
    show_error_user_pass: bool = False
    show_error_existing_user: bool = False
    show_error_address: bool = False
    show_success_changes: bool = False
    user: User = User(name="", surname="", email="", password="", 
                      phone_number="", address_id=None, disabled=False,
                      is_google_user=False)
    address: Address = Address(address = "", city = "", autonomous_community = "", postal_code = "")
    login_cookie: str = rx.Cookie(
        name=const.LOG_IN_COOKIE_NAME, 
        max_age=const.ACCESS_TOKEN_DURATION,
        same_site="lax"
    )
    username: str = rx.Cookie(
        name=const.USERNAME_COOKIE_NAME,
        max_age=const.ACCESS_TOKEN_DURATION,
        same_site="lax"
    )


    def change(self):
        self.show = not (self.show)

    def change_error_user_pass(self):
        self.show_error_user_pass = not (self.show_error_user_pass)

    def change_error_existing_user(self):
        self.show_error_existing_user = not (self.show_error_existing_user)

    def change_error_address(self):
        self.show_error_address = not (self.show_error_address)
    
    def change_success_changes(self):
        self.show_success_changes = not (self.show_success_changes)

    async def log_in(self, form_data: dict):
        try:
            if form_data["password"] is not None:
                token: dict = await api.login_user(form_data)
                self.login_cookie = token.get("access_token")
                self.username = token.get("username")
                self.user = await api.get_user(token.get("access_token"))
            else:
                self.login_cookie = self.tokeninfo["sub"]
                self.username = self.tokeninfo["given_name"]
                self.user = await api.get_user(self.tokeninfo["sub"])
        except Exception:
            self.show_error_user_pass = not (self.show_error_user_pass)

    async def log_in_google(self, data):
        if not self.tokeninfo:
            return rx.redirect(Route.INDEX.value)
        user: User = UserDAO.find_user_by_email(self.tokeninfo["email"])
        if not user:
            name, surname = self.tokeninfo["name"].split(' ', 1)
            form_data = {
                "name": name,
                "surname": surname,
                "email": self.tokeninfo["email"],
                "password": None,
                "address": "",
                "city": "",
                "autonomous_community": "",
                "postal_code": "",
                "phone_number": "",
                "is_google_user": True
            }
            user: User = await api.register_user(form_data)
            self.login_cookie = self.tokeninfo["sub"]
            self.username = name
            self.user = user
            self.change()
        else:
            if user.is_google_user:
                self.login_cookie = self.tokeninfo["sub"]
                self.username = user.name
                self.user = user
                self.change()
            else:
                self.change_error_existing_user()
        
    def log_out(self):
        self.login_cookie = ""
        self.username = ""
    
    async def refresh_user(self):
        try:
            self.user = await api.get_user(self.login_cookie)
        except:
            if self.token_is_valid:
                user_info = self.tokeninfo
                user: User = UserDAO.find_user_by_email(email=user_info["email"])
                self.user = user
            else:
                raise HTTPException(
                    status_code=status.HTTP_401_UNAUTHORIZED,
                    detail="Could not validate credentials",
                    headers={"WWW-Authenticate": "Bearer"},
                )
        if self.user.address_id is not None and self.user.address_id != "":
            self.address = AddressDAO.find_address_by_id(self.user.address_id)  

    async def update_user(self, form_data: dict, id: int):
        user: User = await api.update_user(id, form_data)
        if user is not None:
            self.log_out
            await self.log_in({"username":user.email, "password":user.password})
            self.user = user
            self.change_success_changes()
        
    async def update_address(self, form_data: dict, address_id: int, user_id: int):
        try:
            address: Address = await api.update_address(form_data, address_id, user_id)
        except:
            self.change_error_address()
        if address is not None:
            self.address = address
            self.change_success_changes()
        
    def get_user_address(self):
        return self.user.address_id
    
    def get_user_phone(self):
        return self.user.phone_number
 


# Class that manages the register pop-up
class RegisterState(rx.State):
    show: bool = False
    form_data: dict = {}
    show_error_missing_parameter: bool = False

    def change(self):
        self.show = not (self.show)

    def change_error_missing_parameter(self):
        self.show_error_missing_parameter = not (self.show_error_missing_parameter)

    async def handle_submit(self, form_data: dict):
        if (form_data["name"] == "" or 
                form_data["surname"] == "" or 
                form_data["email"] == "" or 
                form_data["password"] == ""):
            self.change_error_missing_parameter
        else:
            self.form_data = form_data
            self.form_data["is_google_user"] = False
            await api.register_user(self.form_data)