from fastapi import APIRouter, Request
from database.cat_table import cats
from cats.models import CatCreate, CatList
from settings.connection import database
from typing import List, Optional
from fastapi.encoders import jsonable_encoder


route = APIRouter()


@route.post("/cats/create", response_model=CatList)
async def create_cat(cat: CatCreate):
    query = cats.insert().values(
        breed = cat.breed,
        location_of_origin = cat.location_of_origin,
        coat_length = cat.coat_length,
        body_type = cat.body_type,
        pattern = cat.pattern,
    )
    last_record_id = await database.execute(query)
    return { **cat.dict(), 'id': last_record_id}


@route.get("/cats", response_model=List[CatList])
async def list_all_cats():
    query = cats.select()
    return await database.fetch_all(query)


@route.delete("/cats/{id}")
async def delete_cat(id: int):
    query = cats.delete().where(cats.c.id == id)
    await database.execute(query)
    return {"message": "O gato de id: {} foi deletado com sucesso".format(id)}


@route.put("/cats/{id}", response_model=CatList)
async def update_cat(id: int, cat: CatCreate):
    query = cats.update().where(cats.c.id==id).values( 
                                                        breed = cat.breed,
                                                        location_of_origin = cat.location_of_origin,
                                                        coat_length = cat.coat_length,
                                                        body_type = cat.body_type,
                                                        pattern = cat.pattern,
                                                    )
    await database.execute(query)
    return {**cat.dict(), "id":id}


@route.patch("/cats/{id}", response_model=CatList)
async def partial_update_cat(id: int, cat: CatCreate):
    query = cats.select().where(cats.c.id==id)
    cat_infos = await database.fetch_one(query)
    stored_cat_data = cat_infos
    stored_cat_model = CatCreate(**stored_cat_data)
    update_data = cat.dict(exclude_unset=True)
    updated_cat = stored_cat_model.copy(update=update_data)
    cat_infos = jsonable_encoder(updated_cat)

    partial_update = cats.update().where(cats.c.id==id).values(cat_infos)
    await database.execute(partial_update)
    return {**cat.dict(), "id":id}


@route.get("/cats/")
async def search_cat( id: int = None, breed: str = None, location_of_origin: str = None, coat_length: str = None,
                      body_type: str = None, pattern: str = None ):
    
    if id:
        query = cats.select().where(cats.c.id==id)        

    if breed:
        query = cats.select().where(cats.c.breed==breed)

    if location_of_origin:
        query = cats.select().where(cats.c.location_of_origin==location_of_origin)

    if coat_length:
        query = cats.select().where(cats.c.coat_length==coat_length)

    if body_type:
        query = cats.select().where(cats.c.body_type==body_type)

    if pattern:
        query = cats.select().where(cats.c.pattern==pattern)
    
    response = await database.fetch_one(query)
    return response if response else {"Nao": "encontrado"}
