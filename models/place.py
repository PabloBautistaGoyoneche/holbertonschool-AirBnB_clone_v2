#!/usr/bin/python3
""" Place Module for HBNB project """
from os import getenv
from models.base_model import BaseModel, Base
from models.review import Review
from sqlalchemy import Column, String, Integer, Float, ForeignKey, Table
from sqlalchemy.orm import relationship

class Place(BaseModel, Base):
    """ A place to stay """
    __tablename__ = 'places'

    city_id = Column(String(60), ForeignKey('cities.id'), nullable=False)
    user_id = Column(String(60), ForeignKey('users.id'), nullable=False)
    name = Column(String(128), nullable=False)
    description = Column(String(1024), nullable=True)
    number_rooms = Column(Integer, nullable=False, default=0)
    number_bathrooms = Column(Integer, nullable=False, default=0)
    max_guest = Column(Integer, nullable=False, default=0)
    price_by_night = Column(Integer, nullable=False, default=0)
    latitude = Column(Float, nullable=True)
    longitude = Column(Float, nullable=True)
    amenity_ids = []

    if getenv('HBNB_TYPE_STORAGE') == 'db':
        """ Database storage: Establishing relationships """
        reviews = relationship("Review", backref="place", cascade="all, delete-orphan")
    else:
        """ File storage: Getter attribute for reviews """
    @property
    def reviews(self):
        """
        Getter attribute for reviews

        Returns:
            list: List of Review instances associated with the current Place
        """
        from models import storage
        """ We get all objects of type Review from storage """
        all_reviews = storage.all(Review)
        """ We filter reviews that have place_id equal to the ID of this Place """
        place_reviews = [review for review in all_reviews.values()
                        if review.place_id == self.id]
        return place_reviews