from fastapi import APIRouter
from database.cat_table import cats
from cats.models import CatCreate, CatList
from settings.connection import database


route = APIRouter()


@route.post("/cat/create", response_model=CatList)
async def createCat(cat: CatCreate):
    query = cats.insert().values(
        breed = cat.breed,
        location_of_origin = cat.location_of_origin,
        coat_length = cat.coat_length,
        body_type = cat.body_type,
        pattern = cat.pattern,
    )
    last_record_id = await database.execute(query)
    return { **cat.dict(), 'id': last_record_id}