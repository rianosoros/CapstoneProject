from  app import db  # Import the SQLAlchemy instance from your Flask app
from models import User, LikedDrink  # Import your models

# Create the tables
db.create_all()
