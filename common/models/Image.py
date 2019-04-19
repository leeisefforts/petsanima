from sqlalchemy import Column, DateTime, Integer, String
from sqlalchemy.schema import FetchedValue

from managers import db


class Image(db.Model):
    __tablename__ = 'images'

    id = db.Column(Integer, primary_key=True)
    file_key = db.Column(String(60), nullable=False, server_default=FetchedValue())
    created_time = db.Column(DateTime, nullable=False, server_default=FetchedValue())
