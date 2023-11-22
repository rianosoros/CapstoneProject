from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base
from flask_sqlalchemy import SQLAlchemy
from flask_login import UserMixin

db = SQLAlchemy() 

Base = declarative_base()

class User(db.Model, UserMixin):
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    hashed_password = db.Column(db.String(200), nullable=False)
    
    # Relationship to liked drinks
    liked_drinks = relationship("LikedDrink", back_populates="user")
    def get_id(self):
        return str(self.id)

class LikedDrink(db.Model):
    __tablename__ = "liked_drinks"

    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey("users.id"))
    drink_id = Column(String)
    
    # Relationship to user
    user = relationship("User", back_populates="liked_drinks")
    