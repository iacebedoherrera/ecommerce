import reflex as rx
from ecommerce.dal.models.user import Address


class AddressDAO:

    # Insert a new user
    def insert(address: Address):
        with rx.session() as session:
            session.add(address)
            session.commit()
            session.refresh(address)
            return address.id

    # Find a user from the email
    def find_address_by_id(id: int):
        with rx.session() as session:
            return session.exec(Address.select().where(Address.id == id)).first()


    def find_all_address():
        with rx.session() as session:
            return session.exec(Address).all()


    def update_address(id: int, new_data: dict):
        with rx.session() as session:
            address: Address = session.exec(Address.select().where(Address.id == id)).first()
            if address:
                for key, value in new_data.items():
                    setattr(address, key, value)

                session.commit()
                session.refresh(address)
                return address