from sqlalchemy import *
from flask_sqlalchemy import SQLAlchemy
import json
import os
from sqlalchemy.orm import backref, relationship

database_path = os.environ.get('DATABASE_URL')
if not database_path:
    database_name = "agency"
    database_path = "postgresql://{}:{}@{}/{}".format(
        'postgres', '571632', 'localhost:5432', database_name)

db = SQLAlchemy()


def setup_db(app, database_path=database_path):
    app.config["SQLALCHEMY_DATABASE_URI"] = database_path
    app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
    db.app = app
    db.init_app(app)
    db.create_all()


############# Movie Items - assocation table ################
movie_items = db.Table('movie_items',
                       Column('movie_id', Integer, ForeignKey(
                           'Movie.id'), primary_key=True),
                       Column('actor_id', Integer, ForeignKey(
                           'Actor.id'), primary_key=True)
                       )


###################### Movies Model ############################
class Movie(db.Model):
    __tablename__ = 'Movie'

    id = Column(Integer, primary_key=True)
    title = Column(String)
    release_date = Column(DateTime)

    actors = relationship('Actors', backref=backref(
        'Movie', lazy=True), secondary=movie_items)

    def __init__(self, title, release_date, actors):
        self.title = title
        self.release_date = release_date
        self.actors = actors

    def format(self):
        return {
            'id': self.id,
            'name': self.name,
            'release_date': self.release_date,
            'actors': self.actors
        }

    def insert(self):
        db.session.add(self)
        db.session.commit()

    def update(self):
        db.session.commit()

    def delete(self):
        db.session.delete(self)
        db.session.commit()


###################### Actors Model ############################
class Actor(db.Model):
    __tablename__ = "Actor"

    id = Column(Integer, primary_key=True)
    name = Column(String)
    age = Column(Integer)
    gender = Column(Enum('M', 'F'))

    movies = relationship('Movies', backref=backref(
        'Actor', lazy=True), secondary=movie_items)

    def __init__(self, name, age, gender, movies):
        self.name = name
        self.age = age,
        self.gender = gender
        self.movies = movies

    def format(self):
        return {
            'id': self.id,
            'name': self.name,
            'age': self.age,
            'gender': self.gender,
            'movies': self.movies
        }

    def insert(self):
        db.session.add(self)
        db.session.commit()

    def update(self):
        db.session.commit()

    def delete(self):
        db.session.delete()
        db.session.commit()
