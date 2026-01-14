from fastapi import FastAPI , Depends
from app.auth import router as auth_router
from app.kitchen import router as kitchen_router
from app.FoodItems import router as fooditem_router
from app.config import Base , engine

# App initialized
app = FastAPI(title="Food_tracker")

# Cors setup 

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
# Allow requests from your frontend
origins = [
    "http://localhost:19006",   # Expo dev server URL
    "http://127.0.0.1:19006",   # Another common Expo dev URL
    "http://192.168.1.5:19006", # Your computer's IP + Expo port (replace with your IP)
    "*"                         # Optional: allow all origins (useful for testing)
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,  # list of allowed origins
    allow_credentials=True,
    allow_methods=["*"],    # allow GET, POST, PUT, DELETE
    allow_headers=["*"],    # allow all headers
)


# # Table creation without using alembic but i will use alembic so i will comment this 
# Base.metadata.create_all(bind = engine)  


# api endpoints
app.include_router(auth_router , prefix= "/auth" , tags=["auth"])
app.include_router(kitchen_router , prefix="/kitchens" ,tags=["kitchens"])
app.include_router(fooditem_router , prefix="/fooditem" , tags = ["fooditem"])
# dependecy 








