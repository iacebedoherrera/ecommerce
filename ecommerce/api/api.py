import reflex as rx
from ecommerce.dal.models.user import User
from ecommerce.dal.models.user import Address
from .UserAPI import UserAPI
from ecommerce.dal.dao.UserDAO import UserDAO
from ecommerce.dal.dao.AddressDAO import AddressDAO


USER_API = UserAPI()


async def get_user(token: str) -> User:
    user =  await USER_API.get_current_user(token)
    if user.disabled:
        return None
    return user


async def register_user(form_data: dict):
    address = Address(
        address=form_data["address"],
        city=form_data["city"],
        autonomous_community=form_data["autonomous_community"],
        postal_code=form_data["postal_code"]
    )
    address_id = AddressDAO.insert(address)
    user = User(
        name=form_data["name"],
        surname=form_data["surname"],
        email=form_data["email"],
        password=form_data["password"],
        address_id=address_id,
        phone_number=form_data["phone_number"]
    )
    USER_API.register_user(user)


class OauthForm(rx.Base):
    username: str
    password: str


async def login_user(form_data: dict) -> dict:
    oauth_form = OauthForm(
        username=form_data.get("username"), password=form_data.get("password")
    )
    return await USER_API.login_for_access_token(oauth_form)


async def get_address(id: int) -> Address:
    return AddressDAO.find_address_by_id(id)


def update_user(id: str, new_data: dict):
    # Borramos todas las entradas vacias del diccionario
    for clave, valor in list(new_data.items()):
        if valor == "":
            del new_data[clave]

    return UserDAO.update_user(id, new_data)


def update_address(new_data: dict, address_id: int, user_id: int):
    for clave, valor in list(new_data.items()):
        if valor == "":
            del new_data[clave]

    address: Address = AddressDAO.update_address(address_id, new_data)
    return update_user(user_id, {"address_id": address.id})
