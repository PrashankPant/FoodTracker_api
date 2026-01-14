from fastapi import Depends,APIRouter , UploadFile ,File , Form, HTTPException
from schemas.FoodItems import FoodItemCreate , FoodItemResponse 
from sqlalchemy.orm import Session
from app.config import get_db , UPLOAD_DIR
from models.FoodItems import FoodItemsModel
from datetime import date
import os,shutil,uuid
from typing import List , Optional
from enum import Enum
from app.utils import linear_search ,quick_sort
router = APIRouter()

@router.post("/" , response_model= FoodItemResponse , status_code=201)
async def create_fooditem(image:UploadFile = File(...) ,
                        fooditem_name: str = Form(...),
                        expirary_date:date = Form(...),
                        quantity_value:int = Form(...),
                        quantity_unit:str =Form(...),
                        kitchen_id : int = Form(...),  
                        db:Session = Depends(get_db)):
    
    try:
        unique_filename = f"{uuid.uuid4().hex}_{image.filename}"
        file_path = os.path.join(UPLOAD_DIR , unique_filename)
        
        with open(file_path , "wb") as buffer:
            shutil.copyfileobj(image.file , buffer)
        
        fooditem = FoodItemCreate(
            fooditem_name= fooditem_name,
            expirary_date= expirary_date,
            quantity_value= quantity_value,
            quantity_unit=quantity_unit,
            kitchen_id= kitchen_id,
            
        )

        db_fooditem = FoodItemsModel(
            **fooditem.model_dump(),
            fooditem_image = file_path
        )
        db.add(db_fooditem)
        db.commit()
        db.refresh(db_fooditem)

        # return {"msg" : "fooditem created"}    good api return created value
        return db_fooditem
    except Exception as e:
        db.rollback()
        raise HTTPException(status_code=500 , detail=str(e))


   



@router.get("/", response_model=List[FoodItemResponse])
async def get(
    kitchen_id: int,
    search_query: Optional[str] = None,
    sort_query: Optional[str] = None,
    offset: int = 0,
    db: Session = Depends(get_db)
):
    limit = 5
    
    # Fetch ALL items from the database 
    fooditems = db.query(FoodItemsModel).filter(
        FoodItemsModel.kitchen_id == kitchen_id
    ).all()
    
    # Convert to list of dicts for algorithm processing
    items_list = [item.__dict__ for item in fooditems]
    
    # If search is requested
    if search_query:
        # Get all items matching search
        search_results = linear_search(search_query, items_list)
        
        # If sort is also requested, apply sorting to search results
        if sort_query:
            search_results = quick_sort(search_results, sort_query)
        
        # Apply pagination
        start_idx = offset
        end_idx = offset + limit
        paginated_results = search_results[start_idx:end_idx]
        
        # # Convert back to model instances
        # result_ids = [item['fooditem_id'] for item in paginated_results]
        # return db.query(FoodItemsModel).filter(FoodItemsModel.fooditem_id.in_(result_ids)).all()

        return [FoodItemResponse(**item) for item in paginated_results]
    
    # If only sort is requested (no search)
    elif sort_query:
        sorted_items = quick_sort(items_list, sort_query)
        
        # Apply pagination
        start_idx = offset
        end_idx = offset + limit
        paginated_results = sorted_items[start_idx:end_idx]
        
        # # Convert back to model instances
        # result_ids = [item['fooditem_id'] for item in paginated_results]
        # return db.query(FoodItemsModel).filter(FoodItemsModel.fooditem_id.in_(result_ids)).all()

        return [FoodItemResponse(**item) for item in paginated_results]
    
    # Default case: no search, no sort
    else:
        return db.query(FoodItemsModel).filter(
            FoodItemsModel.kitchen_id == kitchen_id
        ).order_by(FoodItemsModel.expirary_date).offset(offset).limit(limit).all()    




