from flask_sqlalchemy import SQLAlchemy
from flask_login import UserMixin

db = SQLAlchemy()


class User(UserMixin, db.Model):
    """ User model """

    __tablename__ = "users"
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(), unique=True, nullable=False)
    email = db.Column(db.String(), unique=True, nullable=False)
    name = db.Column(db.String,nullable=False)
    password = db.Column(db.String, nullable=False)
    hashed_pswd = db.Column(db.String(), nullable=False)
    major = db.Column(db.String)

class Messages(db.Model):
    """ Messages model """

    __tablename__ = "messages"
    id = db.Column(db.Integer, primary_key=True)
    messages = db.Column(db.String())
    time_stamp = db.Column(db.String())
    username = db.Column(db.String())
    room = db.Column(db.String, nullable=False)
