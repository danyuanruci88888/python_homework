from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base

DATABASE_URL = "mysql+pymysql://root:123456@localhost:3306/ai_class?charset=utf8mb4"

engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(bind = engine , autocommit = False,autoflush = False)
Base = declarative_base()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
