from sqlalchemy import Column , Integer , String , ForeignKey
from sqlalchemy.orm import relationship
from app.config import Base


class KitchenModel(Base):
    __tablename__ = "Kitchen"
    kitchen_id = Column(Integer , primary_key=True , index=True)
    kitchen_name = Column(String , nullable=False )
    owner_id = Column(Integer,ForeignKey("project_users.user_id") , nullable=False)
    
    # Keep the both table in sync
    owner = relationship("UserModel" , back_populates="kitchens") 
    food_items = relationship("FoodItemsModel" , back_populates="kitchen")




