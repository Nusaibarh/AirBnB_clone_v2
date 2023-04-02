#!/usr/bin/python3
""" Place Module for HBNB project """
from models.base_model import BaseModel, Base
from models.review import Review
from models.amenity import Amenity

from sqlalchemy import Table, Column, String, ForeignKey, Integer, Float
from sqlalchemy.orm import relationship


class Place(BaseModel,Base):
    """ A place to stay """
    __tablename__ = "places"
    city_id = Column(String(60), ForeignKey("cities.id"), nullable=False)
    user_id = Column(String(60), ForeignKey("users.id"), nullable=False)
    name = Column(String(128), nullable=False)
    description = Column(String(1024))
    number_rooms = Column(Integer, nullable=False, default=0)
    number_bathrooms = Column(Integer, nullable=False, default=0)
    max_guest = Column(Integer, nullable=False, default=0)
    price_by_night = Column(Integer, nullable=False, default=0)
    latitude = Column(Float)
    longitude = Column(Float)
    reviews = relationship("Review", backref="user", cascade="all, delete")
    amenity_ids = []

    place_amenity = Table('place_amenity', Base.metadata,
                    Column('place_id', String(60), ForeignKey("places.id"), nullable=False, primary_key=True),
                    Column('amenity_id', String(60), ForeignKey("amenities.id"), nullable=False, primary_key=True)
                          )
    amenities = relationship("Amenity", viewonly=False, secondary=place_amenity)

    @property
    def reviews(self):
        """create a relationship for state in Filestorage"""
        from models import FileStorage
        amenity_ids = []
        fs = FileStorage()
        placeinstance = fs.all(Place)
        for place in placeinstance:
            if placeinstance[place].place_id is self.id:
                amenity_ids.append(placeinstance[place])
        return (amenity_ids)
