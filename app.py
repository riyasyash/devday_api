import falcon

from controllers.speakers_controller import SpeakersController
from db_manage import Session
from db_session_manager import SQLAlchemySessionManager

app = application = falcon.API(middleware=[
    SQLAlchemySessionManager(Session),
])
speaker = SpeakersController()
app.add_route('/speakers', speaker)