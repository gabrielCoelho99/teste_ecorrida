# models.py
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

def create_user_model():
  """
  Creates and returns the User model class.
  """
  class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(50), nullable=False)
    email = db.Column(db.String(120), nullable=False, unique=True)
    age = db.Column(db.Integer, nullable=False)
    password = db.Column(db.String(128), nullable=False)

  return User