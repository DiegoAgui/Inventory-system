from pydantic import BaseModel, Field
from typing import Optional


class Supplier (BaseModel):
    id : Optional[int]
    sub_name : str = Field(max_length=40,min_length=2,description="supplier name")
    address : str = Field(max_length=40,min_length=2,description="supplier address")
    phone : int = Field(ge=5)
    email : str = Field(max_length=40,min_length=2,description="supplier email")

    class Config:
        schema_extra = {
            "example":{
                "id":1,
                "sub_name":"Bimbo",
                "address":"P. Sherman, calle Wallaby, 42, Sydney",
                "phone":6017500500,
                "email":"example123@gmail.com"
            
            }
        }