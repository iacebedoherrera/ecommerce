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


dotenv.load_dotenv()


# Class that manages the login pop-up
class LoginState(GoogleAuthState):
    show: bool = False
    show_error: bool = False
    user: User = User(name="", surname="", email="", password="", 
                      phone_number="", address_id=None, disabled=False)
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

    def change_error(self):
        self.show_error = not (self.show_error)

    async def log_in(self, form_data: dict):
        try:
            token: dict = await api.login_user(form_data)
            self.login_cookie = token.get("access_token")
            self.username = token.get("username")
        except Exception:
            self.show_error = not (self.show_error)

    async def log_in_google(self, data):
        if not self.tokeninfo:
            return rx.redirect(f"{Route.PRODUCTS.value}/tshirt")
        user = UserDAO.find_user_by_email(self.tokeninfo["email"])
        name, surname = self.tokeninfo["name"].split(' ', 1)
        if not user:
            form_data = {
                "name": name,
                "surname": surname,
                "email": self.tokeninfo["email"],
                "password": "",
                "address_id": "",
                "phone_number": ""
            }
            await api.register_user(form_data)

        self.login_cookie = self.tokeninfo["sub"]
        self.username = name
        self.change()
        
    def log_out(self):
        self.login_cookie = ""
        self.username = ""
    
    async def refresh_user(self):
        self.user = await api.get_user(self.login_cookie)
        if (self.user.address_id != ""):
            self.address = AddressDAO.find_address_by_id(self.user.address_id)  

    async def save_user(self):
        UserDAO.insert(self.user)
        rx.redirect(Route.MY_ACCOUNT.value)

    async def update_user(self, form_data: dict, id: int):
        user: User = api.update_user(id, form_data)
        if user is not None:
            self.log_out
            await self.log_in({"username":user.email, "password":user.password})
            return rx.redirect(Route.MY_ACCOUNT.value)
        
    async def update_address(self, form_data: dict, address_id: int, user_id: int):
        address: Address = api.update_address(form_data, address_id, user_id)
        if address is not None:
            self.address = address
            return rx.redirect(Route.MY_ACCOUNT.value)
        
    def no_mandatory_attribute(self):
        if self.user.address_id is None or self.user.phone_number == "":
            return True
        return False
 


# Class that manages the register pop-up
class RegisterState(rx.State):
    show: bool = False
    form_data: dict = {}

    def change(self):
        self.show = not (self.show)

    async def handle_submit(self, form_data: dict):
        self.form_data = form_data
        await api.register_user(self.form_data)