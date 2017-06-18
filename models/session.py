from sqlalchemy import Column
from sqlalchemy import Integer
from sqlalchemy import String

from db_manage import Base
from helpers.db_helper import DBHelper


class Session(Base):
    __tablename__ = 'sessions'

    id = Column(Integer, primary_key=True)
    topic = Column(String(100))
    description = Column(String(250))

    def __init__(self, topic, description=None):
        self.topic = topic
        self.description = description if description else ""

    def as_json(self):
        return {
            "id": self.id,
            "topic": self.topic,
            "description": self.description
        }

    def create(self, session):
        return DBHelper().create(self, session)

    def update(self, session, update_hash):
        return DBHelper().update(self, session, update_hash)

    def delete(self,session):
        return DBHelper().delete(self, session)
