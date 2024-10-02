import reflex as rx
from datetime import datetime
from pydantic import BaseModel
from ecommerce.dal.models.user import User
from ecommerce.dal.models.user import Address
from ecommerce.dal.models.order import Order
from .UserAPI import UserAPI
from .ProductAPI import ProductAPI
from ecommerce.dal.dao.UserDAO import UserDAO
from ecommerce.dal.dao.AddressDAO import AddressDAO
from fastapi import Path
import os
import ecommerce.const as const
from .PayPalAPI import PayPalAPI, OrderBody
from ecommerce.type_table.order_status import OrderStatus
from ecommerce.dal.dao.OrderDAO import OrderDAO
from ecommerce.dal.dao.OrderItemDAO import OrderItemDAO
from ecommerce.dal.models.order_item import OrderItem


user_api = UserAPI()
paypal_api = PayPalAPI()
product_api = ProductAPI()


async def get_user(token: str) -> User:
    user =  await user_api.get_current_user(token)
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
    if address.address == "":
        address_id = None
    else:
        existing_address: Address = AddressDAO.find_address_by_address_and_city(address.address, address.city)
        if existing_address is None:
            address_id = AddressDAO.insert(address)
        else:
            address_id = existing_address.id
    user = User(
        name=form_data["name"],
        surname=form_data["surname"],
        email=form_data["email"],
        password=form_data["password"],
        address_id=address_id,
        phone_number=form_data["phone_number"],
        is_google_user=form_data["is_google_user"]
    )
    user_api.register_user(user)


class OauthForm(rx.Base):
    username: str
    password: str


async def login_user(form_data: dict) -> dict:
    oauth_form = OauthForm(
        username=form_data.get("username"), password=form_data.get("password")
    )
    try:
        return await user_api.login_for_access_token(oauth_form)
    except Exception as e:
        raise e


async def get_address(id: int) -> Address:
    return AddressDAO.find_address_by_id(id)


async def update_user(id: str, new_data: dict):
    # Borramos todas las entradas vacias del diccionario
    for clave, valor in list(new_data.items()):
        if valor == "":
            del new_data[clave]

    return UserDAO.update_user(id, new_data)


async def update_address(new_data: dict, address_id: int, user_id: int):
    if address_id is not None:
        existing_address: Address = AddressDAO.find_address_by_id(address_id)
        address_inserted: Address = Address(
                                    address=new_data["address"],
                                    city=new_data["city"],
                                    autonomous_community=new_data["autonomous_community"],
                                    postal_code=new_data["postal_code"],
                                )
        compare_address_for_empty_parameter(existing_address, address_inserted)
        for clave, valor in list(new_data.items()):
            if valor == "":
                del new_data[clave]
        
        address: Address = AddressDAO.update_address(address_id, new_data)
    else:
        address_to_save: Address = Address(
                                    address=new_data["address"],
                                    city=new_data["city"],
                                    autonomous_community=new_data["autonomous_community"],
                                    postal_code=new_data["postal_code"],
                                )
        address: Address = AddressDAO.find_address_by_address_and_city(address_to_save.address, address_to_save.city)
        if address is None:
            address: Address = AddressDAO.insert_and_return(address_to_save)
    
    await update_user(user_id, {"address_id": address.id})
    return address


def compare_address_for_empty_parameter(existing_address: Address, address_inserted: Address):
    if address_inserted.address == "":
        if existing_address.address == "":
            raise Exception("Bad Parameters")
    
    if address_inserted.city == "":
        if existing_address.city == "":
            raise Exception("Bad Parameters")
        
    if address_inserted.autonomous_community == "":
        if existing_address.autonomous_community == "":
            raise Exception("Bad Parameters")
        
    if address_inserted.postal_code == "":
        if existing_address.postal_code == "":
            raise Exception("Bad Parameters")


def get_product_images(product_type: str = Path(..., title="Tipo producto"),
                       partnumber: str = Path(..., title="Partnumber")):
    path = os.path.join(product_type, partnumber)
    full_path = os.path.join(const.IMAGES_ROUTE, path)
    if os.path.isdir(full_path):
        image_paths = [os.path.join(path, f) for f in os.listdir(full_path) if os.path.isfile(os.path.join(full_path, f))]
        return {"image_paths": image_paths}
    else:
        return {"message": "Ruta de imágenes no encontrada"}


def create_order(orderBody: OrderBody):
    return paypal_api.create_order(orderBody).json()

def capture_order(order_id):
    return paypal_api.capture_order(order_id).json()


class TokenRequest(BaseModel):
    token: str
    items: dict

async def save_order(request: TokenRequest):
    # Faltaria comprobar si realmente se hizo el pago con una peticion a la api de paypal
    user: User = await get_user(request.token)
    order: Order = Order(
        user_id=user.id,
        address_id=user.address_id,
        creation_date=datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
        status_id=OrderStatus.CREATED.value
    )
    order_id = OrderDAO.insert(order)
    await save_order_items(request.items, order_id)
    return {"order_id": order_id}

async def save_order_items(items: dict, order_id: int):
    for sku in items.keys():
        quantity = items.get(sku)
        order_item: OrderItem = OrderItem(
            order_id=order_id,
            partnumber=sku,
            quantity=quantity,
            creation_date=datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        )
        OrderItemDAO.insert(order_item)
        # Restamos del stock
        await product_api.update_quantity_by_partnumber(sku, -quantity)

