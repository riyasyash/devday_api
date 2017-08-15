import falcon
import logging

from falcon_cors import CORS
from controllers.event_sessions_controller import EventSessionsController
from controllers.events_controller import EventsController
from controllers.locations_controller import LocationsController
from controllers.session_speaker_controller import SessionSpeakerController
from controllers.sessions_controller import SessionsController
from controllers.speakers_controller import SpeakersController
from db_manage import Session
from db_session_manager import SQLAlchemySessionManager

cors = CORS(allow_origins_list=['http://localhost:5050'],
            allow_all_headers=True,
            allow_all_methods=True)

app = application = falcon.API(middleware=[
    SQLAlchemySessionManager(Session),cors.middleware
])

speaker_controller = SpeakersController()
app.add_route('/speakers', speaker_controller)
app.add_route('/speakers/{id}', speaker_controller)

location_controller = LocationsController()
app.add_route('/locations', location_controller)
app.add_route('/locations/{id}', location_controller)

sessions_controller = SessionsController()
app.add_route('/sessions', sessions_controller)
app.add_route('/sessions/{id}', sessions_controller)

events_controller = EventsController()
app.add_route('/events', events_controller)
app.add_route('/events/{id}', events_controller)

events_sessions_controller = EventSessionsController()
app.add_route('/events/{id}/sessions',events_sessions_controller)
app.add_route('/events/{id}/sessions/{session_id}',events_sessions_controller)

session_speaker_controller = SessionSpeakerController()
app.add_route('/session/speakers',session_speaker_controller)
app.add_route('/session/speakers/{id}',session_speaker_controller)
