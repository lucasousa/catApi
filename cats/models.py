from pydantic import BaseModel, Field


class CatCreate(BaseModel):
    breed: str                = Field(..., example="Abyssian")
    location_of_origin: str   = Field(..., example="Asia")  
    coat_length: str          = Field(..., example="Short")
    body_type: str            = Field(..., example="Semi-foreign")
    pattern: str              = Field(..., example="Ticked tabby")


class CatList(BaseModel):
    id: int
    breed: str
    location_of_origin: str
    coat_length: str
    body_type: str
    pattern: str