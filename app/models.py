from app import db, login

from flask_login import UserMixin
from sqlalchemy import Column, Integer, String

from werkzeug.security import generate_password_hash, check_password_hash


@login.user_loader
def load_user(id):
    return Admin.query.get(int(id))


class Climb(db.Model):
    id = Column(Integer, primary_key=True)
    climb_name = Column(String(20), index=True)
    location = Column(String(20), index=True)
    picture_path = Column(String(20), index=True)
    description = Column(String(250), index=True)
    getting_there = Column(String(250), index=True)


class Admin(UserMixin, db.Model):
    id = Column(Integer, primary_key=True)
    username = Column(String(64), index=True)
    email = Column(String(120), index=True, unique=True)
    password_hash = Column(String(128))

    def set_password(self, password):
        self.password_hash = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.password_hash, password)