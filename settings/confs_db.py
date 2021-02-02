from pydantic import BaseSettings


class SettingsDB(BaseSettings):
    connection: str
    host: str
    port: str
    username: str
    name: str
    password: str

    class Config():
        env_file = ".env"