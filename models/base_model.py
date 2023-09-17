#!/usr/bin/python3
"""This module defines a base class for all models in our hbnb clone"""
import uuid
from os import getenv
from datetime import datetime
import models
from sqlalchemy import Column, String, DateTime
from sqlalchemy.ext.declarative import declarative_base

# Create Base = declarative_base() before the class definition of BaseModel
Base = declarative_base()


class BaseModel:
    """A base class for all hbnb models"""
    if getenv('HBNB_TYPE_STORAGE') == 'db':
        id = Column(String(60), primary_key=True, default=lambda: str(
            uuid.uuid4()), nullable=False
            )
        created_at = Column(
            DateTime, nullable=False, default=datetime.utcnow()
            )
        updated_at = Column(
            DateTime, nullable=False, default=datetime.utcnow()
            )
    else:
        def __init__(self, *args, **kwargs):
            """Instantiates a new model"""
            if not kwargs:
                self.id = str(uuid.uuid4())
                self.created_at = self.updated_at = datetime.utcnow()
            else:
                if 'updated_at' not in kwargs:
                    kwargs['updated_at'] = datetime.utcnow()
                else:
                    kwargs['updated_at'] = datetime.strptime(
                        kwargs['updated_at'], '%Y-%m-%dT%H:%M:%S.%f'
                        )
                if 'created_at' not in kwargs:
                    kwargs['created_at'] = datetime.utcnow()
                else:
                    kwargs['created_at'] = datetime.strptime(
                        kwargs['created_at'], '%Y-%m-%dT%H:%M:%S.%f'
                        )
                if kwargs.get("__class__"):
                    del kwargs['__class__']
                self.__dict__.update(kwargs)

    def __str__(self):
        """Returns a string representation of the instance"""
        cls = (str(type(self)).split('.')[-1]).split('\'')[0]
        return '[{}] ({}) {}'.format(cls, self.id, self.__dict__)

    def save(self):
        """
        Updates updated_at with the current time when the instance is changed
        """
        from models import storage
        self.updated_at = datetime.utcnow()
        storage.new(self)
        storage.save()

    """
    Updated the to_dict() method of the BaseModel class to
    remove _sa_instance_state if it exists
    """
    def to_dict(self):
        """Convert instance into dict format"""
        dictionary = {}
        dictionary.update(self.__dict__)
        dictionary.update({'__class__':
                           (str(type(self)).split(
                                                '.')[-1]).split('\'')[0]})
        dictionary['created_at'] = self.created_at.isoformat()
        dictionary['updated_at'] = self.updated_at.isoformat()
        dictionary.pop('_sa_instance_state', None)
        return dictionary

    """
    Added a new public instance method delete() to delete the current
    instance from storage
    """
    def delete(self):
        """Deletes the current instance from storage (models.storage)"""
        from models import storage
        key = "{}.{}".format(self.__class__.__name__, self.id)
        storage.delete(self)