from sqlalchemy import Column, DateTime, Integer, String, Text
from sqlalchemy.schema import FetchedValue
from managers import db


class AppErrorLog(db.Model):
    __tablename__ = 'app_error_log'

    id = db.Column(Integer, primary_key=True)
    referer_url = db.Column(String(255), nullable=False, server_default=FetchedValue())
    target_url = db.Column(String(255), nullable=False, server_default=FetchedValue())
    query_params = db.Column(Text, nullable=False)
    content = db.Column(String, nullable=False)
    created_time = db.Column(DateTime, nullable=False, server_default=FetchedValue())
