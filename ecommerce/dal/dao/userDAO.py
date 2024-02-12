import reflex as rx
from ecommerce.dal.models.user import User


class UserDAO:

    # Insert a new user
    def insert(user: User):
        with rx.session() as session:
            session.add(user)
            session.commit()

    # Find a user from the email
    def find_user_by_email(email: str):
        with rx.session() as session:
            return session.exec(User.select.where(User.email == email)).first()


    def find_all_users():
        with rx.session() as session:
            return session.exec(User).all()