from app import db

from sqlalchemy import Column, Integer, String


class Climb(db.Model):
    id = Column(Integer, primary_key=True)
    climb_name = Column(String(20), index=True)
    location = Column(String(20), index=True)
    picture_path = Column(String(20), index=True)
    description = Column(String(250), index=True)
    getting_there = Column(String(250), index=True)
