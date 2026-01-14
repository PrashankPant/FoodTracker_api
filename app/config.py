from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from urllib.parse import quote_plus
from dotenv import load_dotenv
import os
from sqlalchemy.ext.declarative import declarative_base
load_dotenv()

user = os.getenv("user")
user_password = quote_plus(os.getenv("password"))
host = os.getenv("host")
server = os.getenv("server")
database = os.getenv("database")
port = os.getenv("port")

db_url = f"{server}://{user}:{user_password}@{host}:{port}/{database}"

engine = create_engine(db_url)

SessionLocal = sessionmaker(autocommit = False , autoflush= False , bind=engine)



# dependency for injection
def get_db():
    db = SessionLocal()
    try : 
        yield db
    finally :
        db.close()

"""
Usecase of declerative_base function :
1. Define ORM models easily.
2. Store centralized metadata for all tables.
3. Handle relationships between tables.
4. Support schema migrations with Alembic.
5. Reduce boilerplate code.
6. Enable ORM querying with Python objects.
7. Serve as a single reference for all database operations.
"""
Base = declarative_base()


# image upload file for image

BASE_DIR = os.path.dirname(os.path.abspath(__file__))

# Full absolute path for uploads folder
UPLOAD_DIR = os.path.join(BASE_DIR, "uploads")

# Create folder if it does not exist
os.makedirs(UPLOAD_DIR, exist_ok=True)
 