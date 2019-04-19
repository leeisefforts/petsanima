from sqlalchemy import Column, DateTime, Integer, String
from sqlalchemy.schema import FetchedValue
from managers import db, app


class Store_Member(db.Model):
    __tablename__ = 'store_member'

    id = db.Column(Integer, primary_key=True)
    petname = db.Column(String(100), nullable=False, server_default=FetchedValue())
    petage = db.Column(Integer, nullable=False, server_default=FetchedValue())
    petsex = db.Column(Integer, nullable=False, server_default=FetchedValue())
    hostname = db.Column(String(100), nullable=False, server_default=FetchedValue())
    hostphone = db.Column(String(32), nullable=False, server_default=FetchedValue())
    store_id = db.Column(Integer, nullable=False, server_default=FetchedValue())
    status = db.Column(Integer, nullable=False, server_default=FetchedValue())
    updated_time = db.Column(DateTime, nullable=False, server_default=FetchedValue())
    created_time = db.Column(DateTime, nullable=False, server_default=FetchedValue())

    @property
    def status_desc(self):
        return app.config['STATUS_MAPPING'][str(self.status)]

    @property
    def sex_desc(self):
        sex_mapping = {
            "0": "未知",
            "1": "公",
            "2": "母"
        }
        return sex_mapping[str(self.sex)]
