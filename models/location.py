from sqlalchemy import Column
from sqlalchemy import Integer
from sqlalchemy import String

from db_manage import Base
from helpers.db_helper import DBHelper


class Location(Base):
    __tablename__ = 'locations'

    id = Column(Integer, primary_key=True)
    place = Column(String(50))
    location_url = Column(String(250))

    def __init__(self, place, location_url=None):
        self.place = place
        self.location_url = location_url if location_url else "sample_url"

    def as_json(self):
        return {
            "id": self.id,
            "place": self.place,
            "location_url": self.location_url
        }

    def create(self, session):
        return DBHelper().create(self, session)

    def update(self, session, update_hash):
        return DBHelper().update(self, session, update_hash)

    def delete(self,session):
        return DBHelper().delete(self, session)