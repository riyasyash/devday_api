from sqlalchemy import Column
from sqlalchemy import Date
from sqlalchemy import ForeignKey
from sqlalchemy import Integer
from sqlalchemy import String
from sqlalchemy.orm import relationship

from db_manage import Base
from helpers.db_helper import DBHelper
from models.event import Event
from models.session_speaker import SessionSpeaker


class EventSession(Base):
    __tablename__ = 'event_session_speakers'

    id = Column(Integer, primary_key=True)
    fk_session_speaker = Column(Integer, ForeignKey('session_speakers.id'))
    fk_event = Column(Integer, ForeignKey('events.id'))
    date = Column(Date)
    start_time = Column(String(10))
    end_time = Column(String(10))
    session_speaker = relationship(SessionSpeaker)
    event = relationship(Event)

    def __init__(self, fk_session_speaker, fk_event, date, start_time, end_time):
        self.fk_session_speaker = fk_session_speaker
        self.fk_event = fk_event
        self.date = date
        self.start_time = start_time
        self.end_time = end_time

    def as_json(self):
        return {
            "id": self.id,
            "session_speaker": self.session_speaker.as_json(),
            "event": self.event.as_json(),
            "date": self.date,
            "start_time": self.start_time,
            "end_time": self.end_time
        }

    def create(self, session):
        return DBHelper().create(self, session)

    def update(self, session, update_hash):
        return DBHelper().update(self, session, update_hash)
