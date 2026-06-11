import os
from sqlite3 import dbapi2
from dotenv import load_dotenv
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker,declarative_base

load_dotenv()
password = os.getenv('DATABASE_PASSWORD')
DATABASE_USL = f"mysql+pymysql://{password}@localhost:3306/ai_class?charset=utf8mb4"
engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(bind=engine,autocommit=False,autoflush=False)
Base = declarative_base()

def get_db():
    bd = SessionLocal()
    try:
        ylied db
    finally:
        db.close()



