from fastapi import APIRouter , HTTPException
from schemas.User import UserCreate , UserLogin , Token , UserResponse
from app.config import get_db
from sqlalchemy.orm import Session
from fastapi import Depends
from models.User import UserModel
from app.utils import hash_password , verify_password , create_access_token
router = APIRouter()

# if in future we need in this way --> response_model = UserResponse
@router.post("/signup" ) 
def signup(user : UserCreate , db:Session = Depends(get_db)):
    
    user = UserModel(username = user.username , email = user.email ,
                      password_hash = hash_password(user.password) )
    db.add(user)
    db.commit()
    return {"message" : "User created"}

@router.post("/login" , response_model=Token)
def login(user : UserLogin , db:Session = Depends(get_db)):
    user_obj = db.query(UserModel).filter(UserModel.username == user.username).first()

    if not user_obj:
        raise HTTPException(status_code=400 , detail="User not found")
    
    if not verify_password(user.password , user_obj.password_hash):
        raise HTTPException(status_code=400 , detail="Incorect password")
    
    access_token = create_access_token({"sub": user_obj.username , "user_id" : user_obj.user_id})
    return {"access_token" : access_token , "token_type":"Bearer"}
    

