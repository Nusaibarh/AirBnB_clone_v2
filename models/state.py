#!/usr/bin/python3
""" State Module for HBNB project """
from sqlalchemy import Column, String
from sqlalchemy.orm import relationship

from models.base_model import Base, BaseModel
from models.city import City
from models.engine.file_storage import FileStorage


class State(BaseModel, Base):
    """ State class """
    __tablename__ = "states"
    name = Column(String(128), nullable=False)
    cities = relationship("City", backref="state", cascade="all, delete")

    def __init__(self, *args, **kwargs):
        """initializes state"""
        super().__init__(*args, **kwargs)

    @property
    def cities(self):
        """create a relationship for state in Filestorage"""
        Cities = []
        fs = FileStorage()
        cityinstance = fs.all(City)
        for city in cityinstance:
            if cityinstance[city].state_id == self.id:
                Cities.append(cityinstance[city])
        return (Cities)
