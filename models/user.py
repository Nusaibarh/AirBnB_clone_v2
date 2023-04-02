#!/usr/bin/python3
"""This module defines a class User"""
from sqlalchemy import Table, Column, String
from sqlalchemy.orm import relationship
from models.base_model import BaseModel, Base
from models.place import Place


class User(BaseModel, Base):
    """This class defines a user by various attributes"""
    __tablename__ = "users"
    email = Column(String(128), nullable=False)
    password = Column(String(128), nullable=False)
    first_name = Column(String(128))
    last_name = Column(String(128))
    places = relationship("Place", backref="users", cascade="all, delete")
    reviews = relationship("Review", backref="users", cascade="all, delete")
