import json
import os
import sys

import falcon

sys.path.append(os.path.dirname(os.path.abspath(__file__)) + "/..")
from models.session_speaker import SessionSpeaker


class SessionSpeakerController():
    def on_get(self, req, resp):
        try:
            session_speakers = self.session.query(SessionSpeaker).all()
            resp.body = json.dumps([session_speaker.as_json() for session_speaker in session_speakers], ensure_ascii=False)
            resp.status = falcon.HTTP_200
        except Exception as e:
            resp.body = json.dumps({'error': e.message}, ensure_ascii=False)
            resp.status = falcon.HTTP_400

    def on_post(self, req, resp):
        try:
            request_data = json.loads(req.stream.read())
            session_id = request_data.get("session_id")
            speaker_id = request_data.get("speaker_id")
            if not session_id or not speaker_id:
                resp.body = json.dumps({"status":"insufficient data "}, ensure_ascii=False)
                resp.status = falcon.HTTP_400
                return
            session_speaker = SessionSpeaker(fk_session=session_id, fk_speaker=speaker_id).create(self.session)
            resp.body = json.dumps(session_speaker.as_json(), ensure_ascii=False)
            resp.status = falcon.HTTP_200
        except Exception as e:
            resp.body = json.dumps({'error': e.message}, ensure_ascii=False)
            resp.status = falcon.HTTP_400

    def on_put(self, req, resp, id):
        try:
            request_data = json.loads(req.stream.read())
            session_speaker = self.session.query(SessionSpeaker).filter(SessionSpeaker.id == id).first()
            if not session_speaker:
                resp.body = json.dumps({"status":"association not ound"}, ensure_ascii=False)
                resp.status = falcon.HTTP_404
                return
            session_speaker = session_speaker.update(self.session, request_data)
            resp.body = json.dumps(session_speaker.as_json(), ensure_ascii=False)
            resp.status = falcon.HTTP_200
        except Exception as e:
            resp.body = json.dumps({'error': e.message}, ensure_ascii=False)
            resp.status = falcon.HTTP_400

    def on_delete(self,req,resp,id):
        try:
            session_speaker = self.session.query(SessionSpeaker).filter(SessionSpeaker.id == id).first()
            if not session_speaker:
                resp.body = json.dumps({"status":"association not ound"}, ensure_ascii=False)
                resp.status = falcon.HTTP_404
                return
            session_speaker.delete(self.session)
            resp.body = json.dumps({"status":"associateion removed succesfully"}, ensure_ascii=False)
            resp.status = falcon.HTTP_200
        except Exception as e:
            resp.body = json.dumps({'error': e.message}, ensure_ascii=False)
            resp.status = falcon.HTTP_400
