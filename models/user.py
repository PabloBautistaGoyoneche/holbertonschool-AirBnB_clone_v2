#!/usr/bin/python3
from sqlalchemy import Column, String
from models.base_model import BaseModel, Base

class User(BaseModel, Base):
    """This class defines a user by various attributes"""

    """ Table name in the database """
    __tablename__ = 'users'

    """ Column for email (up to 128 characters, not nullable) """
    email = Column(String(128), nullable=False)

    """ Column for password (up to 128 characters, not nullable) """
    password = Column(String(128), nullable=False)

    """ Column for first name (up to 128 characters, nullable) """
    first_name = Column(String(128), nullable=True)

    """ Column for last name (up to 128 characters, nullable) """
    last_name = Column(String(128), nullable=True)
