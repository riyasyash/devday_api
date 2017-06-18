import json
import os
import sys

import falcon

sys.path.append(os.path.dirname(os.path.abspath(__file__)) + "/..")
from models.event_session import EventSession


class EventSessionsController():
    def on_get(self, req, resp, id, session_id=None):
        try:
            if not session_id:
                event_sessions = self.session.query(EventSession).filter(EventSession.fk_event == id).all()
                resp.body = json.dumps([event_session.as_json() for event_session in event_sessions],
                                       ensure_ascii=False)
            if session_id:
                event_session = self.session.query(EventSession).filter(EventSession.id == session_id).first()
                resp.body = json.dumps(event_session.as_json(),ensure_ascii=False)
            resp.status = falcon.HTTP_200
        except Exception as e:
            resp.body = json.dumps({'error': e.message}, ensure_ascii=False)
            resp.status = falcon.HTTP_400


    def on_post(self, req, resp,id):
        try:
            request_data = json.loads(req.stream.read())
            session_speaker_id = request_data.get("session_speaker_id")
            event_id = id
            date = request_data.get("date")
            start_time = request_data.get("start_time")
            end_time = request_data.get("end_time")
            event_session = EventSession(fk_session_speaker=session_speaker_id, fk_event=event_id, date=date,
                                         start_time=start_time, end_time=end_time).create(self.session)
            resp.body = json.dumps(event_session.as_json(), ensure_ascii=False)
            resp.status = falcon.HTTP_200
        except Exception as e:
            resp.body = json.dumps({'error': e.message}, ensure_ascii=False)
            resp.status = falcon.HTTP_400


    def on_put(self, req, resp, id):
        try:
            request_data = json.loads(req.stream.read())
            event_session = self.session.query(EventSession).filter(EventSession.id == id).first()
            event_session = event_session.update(self.session, request_data)
            resp.body = json.dumps(event_session.as_json(), ensure_ascii=False)
            resp.status = falcon.HTTP_200
        except Exception as e:
            resp.body = json.dumps({'error': e.message}, ensure_ascii=False)
            resp.status = falcon.HTTP_400

    def on_delete(self,req,resp,id):
        try:
            event_session = self.session.query(EventSession).filter(EventSession.id == id).first()
            event_session.delete(self.session)
            resp.status = falcon.HTTP_200
        except Exception as e:
            resp.body = json.dumps({'error': e.message}, ensure_ascii=False)
            resp.status = falcon.HTTP_400