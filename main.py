from fastapi import FastAPI
from settings.connection import database
from cats import controllers as CatController


app = FastAPI()


@app.get("/")
def index():
    return {'Mensagem': 'Hello world!'}


@app.on_event("startup")
async def startup():
    await database.connect()


@app.on_event("shutdown")
async def shutdown():
    await database.disconnect()


app.include_router(CatController.route, tags=["Cat"])