#!/usr/bin/python3
""" State Module for HBNB project """
import models
from models.base_model import BaseModel, Base
from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship, backref
from models.city import City
from os import getenv

if getenv('HBNB_TYPE_STORAGE') == 'db':
    class State(BaseModel, Base):
        """ State class """
        __tablename__ = 'states'
        name = Column(String(128), nullable=False)
        cities = relationship(
            "City", backref="state", cascade="all, delete-orphan"
        )
else:
    class State(BaseModel):
        """ State class """
        name = ""

        if getenv('HBNB_TYPE_STORAGE') != 'db':
            @property
            def cities(self):
                """Getter attribute para devolver la lista de objetos
                City vinculados al Estado actual
                """
                city_list = []
                for city in models.storage.all(City).values():
                    if city.state_id == self.id:
                        city_list.append(city)
                return city_list
