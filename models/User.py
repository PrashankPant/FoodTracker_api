from sqlalchemy import Column , Integer ,String 
from app.config import engine
from sqlalchemy.orm import relationship
from app.config import Base

class UserModel(Base):
    
    __tablename__ = "project_users"
    user_id = Column(Integer , primary_key=True , index=True)
    username = Column(String , unique=True , nullable=False , index=True) #index is used for faster searching by username
    email = Column(String , unique=True , nullable=False)
    password_hash = Column(String , nullable=False)
    provider = Column(String , default = "local")
    provider_id = Column(String ,nullable=True)#as the id might be string
    
    # Keep kitchen and project_users in sync
    kitchens =  relationship("KitchenModel" , back_populates="owner")
