#!/usr/bin/python3
"""This module defines a class to manage file storage for hbnb clone"""
import json
import models
from models.base_model import BaseModel
from models.user import User
from models.place import Place
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.review import Review


class FileStorage:
    """ This class manages storage of hbnb models in JSON format """
    __file_path = 'file.json'
    __objects = {}

    def all(self, cls=None):
        """Returns a dictionary of all objects, or only objects of a specific class."""
        if cls is None:
            return self.__objects

        my_dict = {}
        for key, value in self.__objects.items():
            """ Check if the object is an instance of the specified class (cls) """
            if isinstance(value, cls):
                """ If it is, add the object to the new dictionary (my_dict) """
                my_dict[key] = value
        return my_dict

    def new(self, obj):
        """Adds new object to storage dictionary"""
        self.all().update({obj.to_dict()['__class__'] + '.' + obj.id: obj})

    def save(self):
        """Saves storage dictionary to file"""
        with open(FileStorage.__file_path, 'w') as f:
            temp = {}
            temp.update(FileStorage.__objects)
            for key, val in temp.items():
                temp[key] = val.to_dict()
            json.dump(temp, f)

    def reload(self):
        """Loads storage dictionary from file"""
        classes = {
                    'BaseModel': BaseModel, 'User': User, 'Place': Place,
                    'State': State, 'City': City, 'Amenity': Amenity,
                    'Review': Review
                  }
        try:
            temp = {}
            with open(FileStorage.__file_path, 'r') as f:
                temp = json.load(f)
                for key, val in temp.items():
                        self.all()[key] = classes[val['__class__']](**val)
        except FileNotFoundError:
            pass
        
    def delete(self, obj=None):
        """Remove an object from __objects if it is inside."""
        if obj is not None:
            """ Generate the key for the object in the format "ClassName.ObjectID" """
            key = "{}.{}".format(obj.__class__.__name__, obj.id)
            """ Remove the key and associated object from the storage dictionary """
            self.__objects.pop(key, None)

