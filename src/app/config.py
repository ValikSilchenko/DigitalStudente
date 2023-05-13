from os import environ
from dotenv import load_dotenv


load_dotenv()


DB_USER = environ.get("DB_USER")
DB_HOST = environ.get("DB_HOST")
DB_PSWD = environ.get("DB_PSWD")
DB_NAME = environ.get("DB_NAME")
