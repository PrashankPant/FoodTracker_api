from app.config import Base
from sqlalchemy import Column , Integer , String ,Date,ForeignKey
from sqlalchemy.orm import relationship 
class FoodItemsModel(Base):
    __tablename__ = "FoodItem"
    fooditem_id = Column(Integer , primary_key= True , index=True )
    fooditem_name = Column(String , nullable=False ,  index=True)
    fooditem_image = Column(String)
    expirary_date = Column(Date, nullable=True)
    quantity_value = Column(Integer)
    quantity_unit = Column(String)

    kitchen_id = Column(Integer , ForeignKey("Kitchen.kitchen_id") , nullable=False)
    
    kitchen = relationship("KitchenModel" , back_populates="food_items") 
