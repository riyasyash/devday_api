from sqlalchemy import Column
from sqlalchemy import ForeignKey
from sqlalchemy import Integer
from sqlalchemy import String
from sqlalchemy.orm import relationship

from db_manage import Base
from helpers.db_helper import DBHelper
from models.location import Location


class Event(Base):
    __tablename__ = 'events'

    id = Column(Integer, primary_key=True)
    title = Column(String(50))
    description = Column(String(500))
    meetup_link = Column(String(250))
    fk_location_id = Column(Integer, ForeignKey('locations.id'))
    location = relationship(Location)

    def __init__(self, title, fk_location_id, meetup_link, description=None):
        self.title = title
        self.description = description if description else ""
        self.fk_location_id = fk_location_id
        self.meetup_link = meetup_link

    def as_json(self):
        return {
            "id": self.id,
            "title": self.title,
            "description": self.description,
            "meetup_link": self.meetup_link,
            "location": self.location.place
        }

    def create(self, session):
        return DBHelper().create(self, session)

    def update(self, session, update_hash):
        return DBHelper().update(self, session, update_hash)
