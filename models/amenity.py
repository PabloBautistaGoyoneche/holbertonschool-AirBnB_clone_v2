#!/usr/bin/python3
""" Amenity Module for HBNB project """
from os import getenv
from sqlalchemy import Column, String
from sqlalchemy.orm import relationship
from models.base_model import BaseModel, Base

if getenv('HBNB_TYPE_STORAGE') == 'db':
    class Amenity(BaseModel, Base):
        """ Amenity class to store Amenity information """
        __tablename__ = 'amenities'

        name = Column(String(128), nullable=False)

        place_amenities = relationship(
            "Place",
            secondary="place_amenity",
            back_populates="amenities"
        )
else:
    class Amenity(BaseModel):
        name = ""
