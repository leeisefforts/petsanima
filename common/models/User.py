from sqlalchemy import BigInteger, Column, DateTime, Integer, String
from sqlalchemy.schema import FetchedValue
from managers import db


class User(db.Model):
    __tablename__ = 'user'

    id = db.Column(BigInteger, primary_key=True)
    nickname = db.Column(String(100), nullable=False, server_default=FetchedValue())
    mobile = db.Column(String(20), nullable=False, server_default=FetchedValue())
    email = db.Column(String(100), nullable=False, server_default=FetchedValue())
    sex = db.Column(Integer, nullable=False, server_default=FetchedValue())
    avatar = db.Column(String(64), nullable=False, server_default=FetchedValue())
    login_name = db.Column(String(20), nullable=False, unique=True, server_default=FetchedValue())
    login_pwd = db.Column(String(32), nullable=False, server_default=FetchedValue())
    login_salt = db.Column(String(32), nullable=False, server_default=FetchedValue())
    status = db.Column(Integer, nullable=False, server_default=FetchedValue())
    updated_time = db.Column(DateTime, nullable=False, server_default=FetchedValue())
    created_time = db.Column(DateTime, nullable=False, server_default=FetchedValue())