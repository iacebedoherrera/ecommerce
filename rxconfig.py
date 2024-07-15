import reflex as rx
import dotenv
import os
import pymysql

dotenv.load_dotenv()

pymysql.install_as_MySQLdb()

config = rx.Config(
    app_name="ecommerce",
    db_url=os.environ.get("DATABASE_URL")
)