from passlib.context import CryptContext
from jose import jwt 
from datetime import datetime , timedelta ,timezone
import os
from dotenv import load_dotenv
from fastapi.security import OAuth2PasswordBearer
from fastapi import Depends,HTTPException
from sqlalchemy.orm import Session
from app.config import get_db
from models.User import UserModel
import jwt


# Define secret key and algorithm to use 
load_dotenv()
SECRET_KEY = os.getenv("SECRET_KEY")
ALGORITHM = os.getenv("ALGORITHM")




# Define the hashing method context
pwd_context = CryptContext(schemes=["bcrypt"] , deprecated = "auto") #if the algorithm is changed in future

#Hash the password 
def hash_password(password: str):
    return pwd_context.hash(password)
# Verify the password with its hashed value
def verify_password(plain , hashed):
    return pwd_context.verify(plain , hashed)

# Create a access token 
def create_access_token(data: dict, expires_delta: timedelta | None = None):
    to_encode = data.copy()
    expire =  datetime.now(timezone.utc) + (expires_delta or timedelta(minutes=30))
    to_encode.update({"exp": expire})
    return jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM) #creates the string that combines all

# To get current user 

oauth2_schema = OAuth2PasswordBearer(tokenUrl="/auth/login")

def get_current_user(token : str = Depends(oauth2_schema) , db:Session = Depends(get_db)):
    try:
        payload = jwt.decode(token , SECRET_KEY , ALGORITHM)
        user_id : int = payload.get("user_id")
        if not user_id:
            raise HTTPException(status_code=401 , detail= "Invalid authentication crendials")
    except jwt.PyJWTError:
        raise HTTPException(status_code= 401 , detail="Invalid authentication crendials")
    user = db.query(UserModel).filter(UserModel.user_id == user_id).first()
    if not user :
        raise HTTPException(status_code=404 , detail="User not found")
    return user 


# Algorithms 

# linear serach 

def linear_search(query:str , itemsdict: list ) -> list:
     matched_items = []
     query_lower = query.lower().strip()
     for items in itemsdict:
       print(type(items))
       for item in items:
        #   if query_lower == item["fooditem_name"]:
             print(type(item))
             matched_items.append(item)
     return matched_items

#Quick sort   



# from datetime import datetime

# def quick_sort(items, key):
#     if len(items) <= 1:
#         return items

#     def normalize(value):
#         # Numbers (quantity)
#         if isinstance(value, (int, float)):
#             return value

#         # Date string (expiry_date)
#         if isinstance(value, str) and "-" in value:
#             try:
#                 return datetime.strptime(value, "%Y-%m-%d")
#             except ValueError:
#                 pass

#         # String (name or fallback)
#         return str(value).lower()

#     pivot = items[0]
#     pivot_value = normalize(pivot[key])

#     left, right = [], []

#     for item in items[1:]:
#         item_value = normalize(item[key])

      
#         (left if item_value <= pivot_value else right).append(item)

#     return quick_sort(left, key) + [pivot] + quick_sort(right, key)

def quick_sort(items, key):
    if len(items) <= 1:
        return items

    pivot = items[0][key]
    left = [i for i in items[1:] if i[key] <= pivot]
    right = [i for i in items[1:] if i[key] > pivot]

    return quick_sort(left, key) + [items[0]] + quick_sort(right, key)
