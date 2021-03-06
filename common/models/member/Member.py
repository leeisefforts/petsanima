from sqlalchemy import Column, DateTime, Integer, String
from sqlalchemy.schema import FetchedValue
from managers import db, app


class Member(db.Model):
    __tablename__ = 'member'

    id = db.Column(Integer, primary_key=True)
    nickname = db.Column(String(100), nullable=False, server_default=FetchedValue())
    mobile = db.Column(String(11), nullable=False, server_default=FetchedValue())
    sex = db.Column(Integer, nullable=False, server_default=FetchedValue())
    avatar = db.Column(String(200), nullable=False, server_default=FetchedValue())
    salt = db.Column(String(32), nullable=False, server_default=FetchedValue())
    reg_ip = db.Column(String(100), nullable=False, server_default=FetchedValue())
    status = db.Column(Integer, nullable=False, server_default=FetchedValue())
    updated_time = db.Column(DateTime, nullable=False, server_default=FetchedValue())
    created_time = db.Column(DateTime, nullable=False, server_default=FetchedValue())

    @property
    def status_desc(self):
        return app.config['STATUS_MAPPING'][ str( self.status ) ]

    @property
    def sex_desc(self):
        sex_mapping = {
            "0":"未知",
            "1":"男",
            "2":"女"
        }
        return sex_mapping[str(self.sex)]