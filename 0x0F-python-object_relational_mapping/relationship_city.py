#!/usr/bin/python3
"""
this module are contain the infomation of cities class
"""
from relationship_state import Base
from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.ext.declarative import declarative_base


class City(Base):
    """
    this class are containing the table cities
    """
    __tablename__ = 'cities'
    id = Column(Integer, unique=True, nullable=False, primary_key=True)
    name = Column(String(128), nullable=False)
    state_id = Column(Integer, ForeignKey("states.id"), nullable=False)
