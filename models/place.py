#!/usr/bin/python3
""" Place Module for HBNB project """
from os import getenv
from models.base_model import BaseModel, Base
from models.review import Review
from sqlalchemy import Column, String, Integer, Float, ForeignKey, Table
from sqlalchemy.orm import relationship


if getenv('HBNB_TYPE_STORAGE') == 'db':
    """ Defines the place_amenity table for the Many-To-Many relationship """
    metadata = Base.metadata
    place_amenity = Table(
        'place_amenity',
        metadata,
        Column(
            'place_id',
            String(60),
            ForeignKey('places.id'),
            primary_key=True,
            nullable=False
        ),
        Column(
            'amenity_id',
            String(60),
            ForeignKey('amenities.id'),
            primary_key=True,
            nullable=False
        )
    )

    class Place(BaseModel, Base):
        """ Place class to store place information. """
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

        """ Add the relationship amenities with secondary (for DBStorage) """
        amenities = relationship(
            "Amenity",
            secondary=place_amenity,
            viewonly=False,
            back_populates="place_amenities"
        )
        reviews = relationship(
            "Review",
            backref="place",
            cascade="all, delete-orphan"
        )
else:
    class Place(BaseModel):
        """ Add the getter and setter for amenities (for FileStorage) """
        """ A place to stay """
        city_id = ""
        user_id = ""
        name = ""
        description = ""
        number_rooms = 0
        number_bathrooms = 0
        max_guest = 0
        price_by_night = 0
        latitude = 0.0
        longitude = 0.0
        amenity_ids = []

        @property
        def amenities(self):
            """
            Getter attribute for amenities

            Returns:
                list: List of Amenity instances linked to this Place
            """
            from models import storage
            from models.amenity import Amenity
            all_amenities = storage.all(Amenity)
            linked_amenities = []
            for amenity_id in self.amenity_ids:
                key = f"Amenity.{amenity_id}"
                if key in all_amenities:
                    linked_amenities.append(all_amenities[key])
            return linked_amenities

        @amenities.setter
        def amenities(self, amenity):
            """
            Setter attribute for amenities

            Args:
                amenity (Amenity): Amenity object to add to amenity_ids
            """
            from models.amenity import Amenity
            if isinstance(amenity, Amenity):
                self.amenity_ids.append(amenity.id)

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
            """
            We filter reviews that have place_id equal to the ID of this Place
            """
            place_reviews = [
                review for review in all_reviews.values()
                if review.place_id == self.id
            ]
            return place_reviews
