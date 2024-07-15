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
            return session.exec(User.select().where(User.email == email)).first()


    # Find all users
    def find_all_users():
        with rx.session() as session:
            return session.exec(User).all()
        
    
    # Update a user with new_data
    def update_user(user_id: int, new_data: dict):
        with rx.session() as session:
            user: User = session.exec(User.select().where(User.id == user_id)).first()
            if user:
                for key, value in new_data.items():
                    setattr(user, key, value)
                
                session.commit()
                session.refresh(user)
                return user
    