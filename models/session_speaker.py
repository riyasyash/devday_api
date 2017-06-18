from sqlalchemy import Column
from sqlalchemy import ForeignKey
from sqlalchemy import Integer
from sqlalchemy.orm import relationship

from db_manage import Base
from helpers.db_helper import DBHelper
from models.session import Session
from models.speaker import Speaker


class SessionSpeaker(Base):
    __tablename__ = 'session_speakers'

    id = Column(Integer, primary_key=True)
    fk_session = Column(Integer,ForeignKey('sessions.id'))
    fk_speaker = Column(Integer,ForeignKey('speakers.id'))
    speaker = relationship(Speaker)
    session = relationship(Session)

    def __init__(self, fk_session,  fk_speaker):
        self.fk_session = fk_session
        self.fk_speaker = fk_speaker

    def as_json(self):
        return {
            "id": self.id,
            "session": self.session.as_json(),
            "speaker": self.speaker.as_json()
        }

    def create(self, session):
        return DBHelper().create(self, session)

    def update(self, session, update_hash):
        return DBHelper().update(self, session, update_hash)

    def delete(self,session):
        return DBHelper().delete(self, session)