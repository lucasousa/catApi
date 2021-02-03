import databases
import sqlalchemy
from functools import lru_cache
from settings import confs_db
from database.cat_table import metadata


@lru_cache()
def db_infos():
    return confs_db.SettingsDB()


def DATABASE_URL(
    connection: str   = db_infos().connection,
    host: str         = db_infos().host,
    port: str         = db_infos().port,
    username: str     = db_infos().username,
    name: str         = db_infos().name,
    password: str     = db_infos().password,
):
    return str(connection+"://"+username+":"+password+"@"+host+":"+port+"/"+name)


database = databases.Database(DATABASE_URL())


engine = sqlalchemy.create_engine(
    DATABASE_URL()
)

metadata.create_all(engine)