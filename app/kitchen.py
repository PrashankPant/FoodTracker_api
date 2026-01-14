from fastapi import APIRouter,Depends , HTTPException
from schemas.Kitchen import KitchenCreate , KitchenResponse
from sqlalchemy.orm import Session
from app.config import get_db
from models.Kitchen import KitchenModel 
from models.User import UserModel
from app.utils import get_current_user
router = APIRouter()

# api to  create the kitchen 
@router.post("/")
def create_kitchen(kitchen:KitchenCreate , db:Session = Depends(get_db) , current_user = Depends(get_current_user)):
    db_kitchen = KitchenModel(kitchen_name = kitchen.kitchen_name , owner_id = current_user.user_id )
    db.add(db_kitchen)
    db.commit()
    return {"message" : "Kitchen created"}

# api to get all kitchen
@router.get("/" , response_model = list[KitchenResponse] )
def get_all_kitchens(db:Session = Depends(get_db) ,current_user = Depends(get_current_user)):
    kitchen_data =  db.query(KitchenModel).filter(KitchenModel.owner_id == current_user.user_id).all()
    # print(kitchen_data)
    return kitchen_data

# api to get kitchen according to the provided id
# For future 
@router.get("/{id}",response_model=KitchenResponse)
def get_kitchen(kitchen_id:int , db:Session = Depends(get_db)):
    kitchen =  db.query(KitchenModel).filter(KitchenModel.kitchen_id == kitchen_id).first()
    if not kitchen:
        raise HTTPException(status_code=400 , detail="Kitchen not found")
    return kitchen



    
