from sqlalchemy import BigInteger, Column, DateTime, Integer, String
from sqlalchemy.schema import FetchedValue
from managers import db


class Admin_User(db.Model):
    __tablename__ = 'admin_user'

    id = db.Column(db.BigInteger, primary_key=True)
    admin_name = db.Column(db.String(100), nullable=False, server_default=db.FetchedValue())
    admin_pwd = db.Column(db.String(20), nullable=False, server_default=db.FetchedValue())
    admin_salt = db.Column(db.String(100), nullable=False, server_default=db.FetchedValue())
    nickname = db.Column(db.String(64), nullable=False, server_default=db.FetchedValue())
    avatar = db.Column(db.String(64), nullable=False, server_default=db.FetchedValue())
    mobile = db.Column(db.String(20), nullable=False, unique=True, server_default=db.FetchedValue())
    email = db.Column(db.String(32), nullable=False, server_default=db.FetchedValue())
    status = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue())
    updated_time = db.Column(db.DateTime, nullable=False, server_default=db.FetchedValue())
    created_time = db.Column(db.DateTime, nullable=False, server_default=db.FetchedValue())
