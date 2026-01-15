from pydantic import BaseModel , field_validator
from datetime import date
from typing import Literal

class FoodItemBase(BaseModel):
    fooditem_name : str
    # fooditem_image : str will be provide from UploadFile
    expirary_date: date
    quantity_value: int
    quantity_unit :Literal["kg", "gram", "liters", "pieces"]

    @field_validator("expirary_date")
    def expirary_validator(cls , value):
        if value < date.today():
            raise ValueError("Expiry cannot be past date.")
        return value
    
    @field_validator("quantity_value")
    def quantity_validator(cls , value):
        if value <= 0 : 
            raise ValueError("Quantity must be a positive integer.")
        return value

class FoodItemCreate(FoodItemBase):
    # fooditem_id : int as it will be not provided by the frontend
    kitchen_id : int

class FoodItemResponse(FoodItemBase):
    fooditem_id: int
    kitchen_id: int
    fooditem_image: str

    class Config:
        from_attributes = True
        # This allows dict input
        orm_mode = True