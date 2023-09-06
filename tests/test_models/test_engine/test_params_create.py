#!/usr/bin/python3
import unittest
from console import HBNBCommand
from models import storage
from models.base_model import BaseModel

class TestCreateWithParameters(unittest.TestCase):
    def setUp(self):
        """Clean storage before each test"""
        storage.delete_all()
        

if __name__ == "__main__":
    unittest.main()
