#!/usr/bin/python3
"""This module defines a class to manage file storage for hbnb clone"""
import json
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
        """ Returns a dictionary of all objects, or only objects of a specific class """
        """ If no class is specified (cls is None), it returns the entire dictionary of objects """
        if cls is None:
            return FileStorage.__objects
        
        """ Creates an empty dictionary to store objects filtered by class """
        myDict = {}
        
        """ Iterates through all the keys and values ​​in the object dictionary (__objects)"""
        for key, value in FileStorage.__objects.items():
            """ Checks if the class of the object matches the specified class (cls) """
            if (value.__class__ == cls):
                """ If it matches, add the object to the new dictionary (myDict) with the same key and value """
                myDict[key] = value
        
        """ Returns the resulting dictionary, containing objects of the specified class (if cls was provided) """
        return myDict

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
        """ Remove an object from __objects if it is inside """
        if obj is not None:
            """ Creates the key for the object to be deleted in the format "ClassName.ObjectID" """
            bye_key = str(obj.__class__.__name__) + '.' + (obj.id)
            """ Removes the key and associated object from the storage dictionary """
            FileStorage.__objects.pop(bye_key)

