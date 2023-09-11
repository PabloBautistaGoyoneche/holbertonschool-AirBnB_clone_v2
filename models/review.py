#!/usr/bin/python3
""" Review module for the HBNB project """
from models.base_model import BaseModel
from sqlalchemy import Column, String, ForeignKey
from sqlalchemy.orm import relationship


class Review(BaseModel):
    """ Review class to store review information. """
    """ Table name for database storage """
    __tablename__ = 'reviews'

    """ Column for text (up to 1024 characters, not nullable) """
    text = Column(String(1024), nullable=False)

    """ Column for place_id (up to 60 characters, not nullable), foreign key to places.id """
    place_id = Column(String(60), ForeignKey('places.id'), nullable=False)

    """ Column for user_id (up to 60 characters, not nullable), foreign key to users.id """
    user_id = Column(String(60), ForeignKey('users.id'), nullable=False)
