import datetime
import sqlalchemy
from flask_login import UserMixin
from sqlalchemy import orm
from werkzeug.security import generate_password_hash, check_password_hash

from .db_session import SqlAlchemyBase


class Film(SqlAlchemyBase, UserMixin):
    __tablename__ = 'films'

    id = sqlalchemy.Column(sqlalchemy.Integer, primary_key=True, autoincrement=True)
    picture = sqlalchemy.Column(sqlalchemy.String, nullable=True)
    title = sqlalchemy.Column(sqlalchemy.String, nullable=True)
    about = sqlalchemy.Column(sqlalchemy.String, nullable=True)
    date = sqlalchemy.Column(sqlalchemy.String, nullable=True)
    country = sqlalchemy.Column(sqlalchemy.String, nullable=True)
    genre = sqlalchemy.Column(sqlalchemy.String, nullable=True)
    producer = sqlalchemy.Column(sqlalchemy.String, nullable=True)
    director = sqlalchemy.Column(sqlalchemy.String, nullable=True)
    budget = sqlalchemy.Column(sqlalchemy.String, nullable=True)
    box_office = sqlalchemy.Column(sqlalchemy.String, nullable=True)
    length = sqlalchemy.Column(sqlalchemy.String, nullable=True)
    raiting = sqlalchemy.Column(sqlalchemy.Integer, nullable=True)

    news = orm.relationship("News", back_populates='film')

    def __repr__(self):
        return f'<Film> {self.id} {self.title} {self.about}'