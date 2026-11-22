from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import validates
db = SQLAlchemy()

class Author(db.Model):
  __tablename__ = 'authors'
  
  id = db.Column(db.Integer, primary_key=True)
  name= db.Column(db.String, unique=True, nullable=False)
  phone_number = db.Column(db.String)
  created_at = db.Column(db.DateTime, server_default=db.func.now())
  updated_at = db.Column(db.DateTime, onupdate=db.func.now())

  # Add validators 
  
  @validates('name')
  def validate_name(self, key, name):
    if not isinstance(name, str) or not name.strip():
      raise ValueError('Author must have a name')
    return name
  
  @validates('phone_number')
  def validate_phone_number(self, key, phone_number):
    if (
      not isinstance(phone_number, str)
      or len(phone_number) != 10
      or not phone_number.isascii()
      or not phone_number.isdigit()
    ):
      raise ValueError('Phone number must be exactly 10 digits.')
    
  def __repr__(self):
    return f'Author(id={self.id}, name={self.name})'

class Post(db.Model):
    __tablename__ = 'posts'
    
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String, nullable=False)
    content = db.Column(db.String)
    category = db.Column(db.String)
    summary = db.Column(db.String)
    created_at = db.Column(db.DateTime, server_default=db.func.now())
    updated_at = db.Column(db.DateTime, onupdate=db.func.now())

    # Add validators  


    def __repr__(self):
        return f'Post(id={self.id}, title={self.title} content={self.content}, summary={self.summary})'
