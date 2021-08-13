from sqlalchemy import *
from flask_sqlalchemy import SQLAlchemy
import babel
import dateutil.parser
import json
import os


database_name = "casting"
database_path = os.environ['DATABASE_URL']

db = SQLAlchemy()


def setup_db(app, database_path=database_path):
    app.config["SQLALCHEMY_DATABASE_URI"] = database_path
    app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
    db.app = app
    db.init_app(app)
    db.create_all()


###################### Models - Movies Model #########################
class Movie(db.Model):
    __tablename__ = 'movies'

    id = Column(Integer, primary_key=True)
    title = Column(String)
    release_date = Column(DateTime)

    def __init__(self, title, release_date):
        self.title = title
        self.release_date = release_date

    def format(self):
        return {
            'id': self.id,
            'title': self.title,
            'release_date': self.release_date,
        }

    def insert(self):
        db.session.add(self)
        db.session.commit()

    def update(self):
        db.session.commit()

    def delete(self):
        db.session.delete(self)
        db.session.commit()

    # def format_datetime(value, format='medium'):
    #     date = dateutil.parser.parse(value)
    #     if format == 'full':
    #         format="EEEE MMMM, d, y 'at' h:mma"
    #     elif format == 'medium':
    #         format="EE MM, dd, y h:mma"
    #     return babel.dates.format_datetime(date, format, locale='en')

    #     app.jinja_env.filters['datetime'] = format_datetime


###################### Actors Model ############################
class Actor(db.Model):
    __tablename__ = "actors"

    id = Column(Integer, primary_key=True)
    name = Column(String)
    age = Column(Integer)
    gender = Column(Enum('M', 'F', name='gender_types'))

    def __init__(self, name, age, gender):
        self.name = name
        self.age = age,
        self.gender = gender

    def format(self):
        return {
            'id': self.id,
            'name': self.name,
            'age': self.age,
            'gender': self.gender,
        }

    def insert(self):
        db.session.add(self)
        db.session.commit()

    def update(self):
        db.session.commit()

    def delete(self):
        db.session.delete(self)
        db.session.commit()
