#!/usr/bin/python3
"""This is the place class"""
from models.base_model import BaseModel, Base
from os import getenv
import sqlalchemy
from sqlalchemy import Column, String, Integer, Float, ForeignKey
from sqlalchemy.orm import relationship

metadata = Base.metadata

association_table = Table('place_amenity', metadata,
                          Column('place_id', String(60),
                                 ForeignKey(places.id),
                                 primarykey=True,
                                 nullable=False),
                          Column('amenity_id', String(60),
                                 ForeignKey(amenities.id),
                                 primaykey=True,
                                 nullable=False))


class Place(BaseModel, Base):
    """This is the class for Place
    Attributes:
        city_id: city id
        user_id: user id
        name: name input
        description: string of description
        number_rooms: number of room in int
        number_bathrooms: number of bathrooms in int
        max_guest: maximum guest in int
        price_by_night:: pice for a staying in int
        latitude: latitude in flaot
        longitude: longitude in float
        amenity_ids: list of Amenity ids
    """
    __tablename__ = "places"
    city_id = Column(String(60), ForeignKey('cities.id'),
                     nullable=False)
    user_id = Column(String(60), ForeignKey('users.id'),
                     nullable=False)
    name = Column(String(128), nullable=False)
    description = Column(String(1024), nullable=True)
    number_rooms = Column(Integer, default=0, nullable=False)
    number_bathrooms = Column(Integer, default=0,
                              nullable=False)
    max_guest = Column(Integer, default=0, nullable=False)
    price_by_night = Column(Integer, default=0,
                            nullable=False)
    latitude = Column(Float, nullable=True)
    longitude = Column(Float, nullable=True)

    if getenv('HBNB_ENV') == 'db':
        reviews = relationship("Review", backref="place",
                               cascade="all, delete-orphan")

        amenities = relationship("place_amenity",
                                 secondary="Amenity",
                                 viewonly=False)
    else:
        @property
        def reviews(self):
            """returns list of Review instances with place_id equal
            to current Place.id
            """
            objects = models.storage.all(Review)
            review_list = []
            for obj in objects.values():
                if obj.place_id == self.id:
                    review_list.append(obj)
            return review_list

        @property
        def amenities(self):
            """ returns list of Amenity instances"""
            return amenity_ids

        @amenities.setter
        def amenities(self):
            """ stores list of amenities"""
            objects = models.storage.all(Amenity)
            amenity_ids = []
            for obj in objects.values():
                if obj.amenity_id = self.id:
                    amenity_ids.append(obj.id)
