from sqlalchemy import Column
from sqlalchemy import Integer
from sqlalchemy import String

from db_manage import Base
from helpers.db_helper import DBHelper


class Speaker(Base):
    __tablename__ = 'speakers'

    id = Column(Integer, primary_key=True)
    name = Column(String(50))
    dp_url = Column(String(250))
    profile_url = Column(String(250))

    def __init__(self, name, dp_url=None, profile_url=None):
        self.name = name
        self.dp_url = dp_url if dp_url else "sample_url"
        self.profile_url = profile_url if profile_url else "sample_url"

    def create(self,session):
        return DBHelper().create(self,session)

    def update(self, session, update_hash):
        return DBHelper().update(self,session,update_hash)

    def delete(self, session):
        return DBHelper().delete(self, session)

    def as_json(self):
        return {
            "id": self.id,
            "name": self.name,
            "dp_url": self.dp_url,
            "profile_url": self.profile_url
        }
