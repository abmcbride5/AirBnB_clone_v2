#!/usr/bin/python3
"""This is the amenity class"""
from models.base_model import BaseModel
from sqlalchemy import Column, String
import sqlalchemy
from sqlalchemy.orm import relationship

class Amenity(BaseModel):
    """This is the class for Amenity
    Attributes:
        name: input name
    """
    __tablename__ = 'amenities'

    name = Column(String(128), nullable=False)
