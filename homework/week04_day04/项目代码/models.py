from sqlalchemy import Column, Integer, String, ForeignKey, DateTime, Text
from sqlalchemy.sql import func
from database import Base

class User(Base):
    __tablename__ = 'users'

    id = Column(Integer, primary_key=True, index=True)
    username = Column(String(50), unique=True, nullable=False)
    password_hash = Column(String(255), nullable=False)
    created_at = Column(DateTime, server_default=func.now())

class Task(Base):
    __tablename__ = 'tasks'

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String(100), nullable=False)
    status = Column(String(20), nullable=False)
    user_id = Column(Integer, ForeignKey('users.id'), nullable=False)
    created_at = Column(DateTime, server_default=func.now())

class Job(Base):
    __tablename__ = 'jobs'

    id = Column(Integer,primary_key=True,index=True)
    title = Column(String(200),nullable=False)
    company = Column(String(200),nullable=False)
    location = Column(String(100),nullable=True)
    description = Column(Text,nullable=True)
    created_at = Column(DateTime,server_default=func.now())

class Favorite(Base):
    __tablename__ = 'favorites'

    id = Column(Integer,primary_key=True,index=True)
    user_id = Column(Integer,ForeignKey('users.id'),nullable=False)
    job_id = Column(Integer,ForeignKey('jobs.id'),nullable=False)
    created_at = Column(DateTime, server_default=func.now())

class Application(Base):
    __tablename__ = 'applications'

    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey('users.id'), nullable=False)
    job_id = Column(Integer, ForeignKey('jobs.id'), nullable=False)
    status = Column(String(50), default='已投递')
    notes = Column(Text, nullable=True)
    applied_at = Column(DateTime, server_default=func.now())