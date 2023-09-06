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

    def test_create_instance_with_float_parameter(self):
        """Test instantiation with a floating point parameter"""
        cmd = 'create BaseModel price=10.99'
        HBNBCommand().onecmd(cmd)
        obj_id = cmd.split()[2]
        obj = storage.all()["BaseModel." + obj_id]
        self.assertIsInstance(obj, BaseModel)
        self.assertEqual(obj.price, 10.99)

    def test_create_instance_with_multiple_parameters(self):
        """Try creating an instance with multiple parameters"""
        cmd = 'create BaseModel name="My House" age=30 price=99.99'
        HBNBCommand().onecmd(cmd)
        obj_id = cmd.split()[2]
        obj = storage.all()["BaseModel." + obj_id]
        self.assertIsInstance(obj, BaseModel)
        self.assertEqual(obj.name, "My House")
        self.assertEqual(obj.age, 30)
        self.assertEqual(obj.price, 99.99)

    def test_create_instance_with_invalid_parameter_format(self):
        """Try creating an instance with an invalid parameter format"""
        cmd = 'create BaseModel invalid_param'
        output = HBNBCommand().onecmd(cmd)
        self.assertIn("** invalid parameter format:", output)

    def test_create_instance_with_invalid_class_name(self):
        """Try creating an instance with an invalid class name"""
        cmd = 'create InvalidClassName name="My House"'
        output = HBNBCommand().onecmd(cmd)
        self.assertIn("** class doesn't exist **", output)

if __name__ == "__main__":
    unittest.main()
