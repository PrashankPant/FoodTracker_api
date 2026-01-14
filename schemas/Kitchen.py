from pydantic import BaseModel

"""We could have done it in simpler way 
   using one class inheriting the BaseModel or 
   Making one KitchenCreate(BaseModel) but 
   it will be lack clarity and would be 
   hard for maintainig so we choose this 
   to work as fastapi docs"""

"""
The field naming in model should match the naming in
schema or used should map it using

id : int = Field(...,alias = "column_field name)
and also add -> allow_population_by_field_name = True
Lets you use both aliases and field names when creating models

if not done this : it will throw an ResponseValidationError
as pydanctic schema are used for validation of serialization"""

# For making a blueprint 
class KitchenBase(BaseModel):
    kitchen_name :str
   

# id will be auto-generated so no need to have id 
class KitchenCreate(KitchenBase):
    pass

# this is for directly interacting with database
class KitchenResponse(KitchenBase):
    kitchen_id : int
    owner_id : int

    class Config:
        orm_mode = True