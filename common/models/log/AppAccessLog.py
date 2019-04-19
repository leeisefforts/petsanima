from sqlalchemy import BigInteger, Column, DateTime, Integer, String, Text
from sqlalchemy.schema import FetchedValue
from managers import db


class AppAccessLog(db.Model):
    __tablename__ = 'app_access_log'

    id = db.Column(Integer, primary_key=True)
    uid = db.Column(BigInteger, nullable=False, index=True, server_default=FetchedValue())
    referer_url = db.Column(String(255), nullable=False, server_default=FetchedValue())
    target_url = db.Column(String(255), nullable=False, server_default=FetchedValue())
    query_params = db.Column(Text, nullable=False)
    ua = db.Column(String(255), nullable=False, server_default=FetchedValue())
    ip = db.Column(String(32), nullable=False, server_default=FetchedValue())
    note = db.Column(String(1000), nullable=False, server_default=FetchedValue())
    created_time = db.Column(DateTime, nullable=False, server_default=FetchedValue())
