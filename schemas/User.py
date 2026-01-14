from pydantic import BaseModel,EmailStr

# Main user schema
class UserBase(BaseModel):
    username : str
    email : EmailStr

# Inherits UserBase plus password field for signup 
class UserCreate(UserBase):
    password : str

# Only provides response as UserBase with id hiding the plain password
class UserResponse(UserBase):
    id : int

# allows compatibility with SQLAlchemy ORM objects
    class Config : 
        orm_mode = True

# For sing in 
class UserLogin(BaseModel):
    username : str
    password : str

# For token access

class Token(BaseModel):
    access_token : str
    token_type : str
    # refresh_token :str 
