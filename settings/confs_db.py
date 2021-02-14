from pydantic import BaseSettings
from decouple import config

class SettingsDB(BaseSettings):
    connection: str    = config("CONNECTION")
    host: str          = config("HOST")
    port: str          = config("PORT")
    username: str      = config("USERNAME")
    name: str          = config("NAME")
    password: str      = config("PASSWORD")
