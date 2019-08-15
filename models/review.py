#!/usr/bin/python3
"""This is the review class"""
from models.base_model import BaseModel
from sqlalchemy import Column, ForeignKey, String


class Review(BaseModel):
    """This is the class for Review
    Attributes:
        place_id: place id
        user_id: user id
        text: review description
    """
    __tablename__ = "reviews"
    text = Column(String(60), ForeignKey('places.id'),
                  nullable=False)
