import reflex as rx
import dotenv
import os
from sqlalchemy.engine import URL

dotenv.load_dotenv()

config = rx.Config(
    app_name="ecommerce",
    db_url=os.environ.get("DATABASE_URL")
)