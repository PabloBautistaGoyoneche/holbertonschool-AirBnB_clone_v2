#!/usr/bin/python3
import unittest
from console import HBNBCommand
from models import storage
from models.base_model import BaseModel

class TestCreateWithParameters(unittest.TestCase):
    def setUp(self):
        """Clean storage before each test"""
        storage.delete_all()
    
    def tearDown(self):
        """Limpiar el almacenamiento después de cada prueba"""
        storage.delete_all()

    def test_create_instance_with_string_parameter(self):
        """Test creating an instance with a string parameter"""
        cmd = 'create BaseModel name="My little house"'
        HBNBCommand().onecmd(cmd)
        obj_id = cmd.split()[2]  # Obtiene el ID del objeto creado
        obj = storage.all()["BaseModel." + obj_id]
        self.assertIsInstance(obj, BaseModel)
        self.assertEqual(obj.name, "My little house")

    def test_create_instance_with_integer_parameter(self):
        """Test creating an instance with an integer parameter"""
        cmd = 'create BaseModel age=25'
        HBNBCommand().onecmd(cmd)
        obj_id = cmd.split()[2]
        obj = storage.all()["BaseModel." + obj_id]
        self.assertIsInstance(obj, BaseModel)
        self.assertEqual(obj.age, 25)

if __name__ == "__main__":
    unittest.main()
