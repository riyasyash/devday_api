import json
import os

import falcon
import sys

sys.path.append(os.path.dirname(os.path.abspath(__file__)) + "/..")
from models.speaker import Speaker


class SpeakersController():
    def on_get(self, req, resp, id=None):
        try:
            if not id:
                speakers = self.session.query(Speaker).all()
                resp.body = json.dumps([speaker.as_json() for speaker in speakers], ensure_ascii=False)
            else:
                speaker = self.session.query(Speaker).filter(Speaker.id == id).first()
                if not speaker:
                    resp.body = json.dumps({"status":"speaker not found"}, ensure_ascii=False)
                    resp.status = falcon.HTTP_200
                    return
                resp.body = json.dumps(speaker.as_json(), ensure_ascii=False)
            resp.status = falcon.HTTP_200
        except Exception as e:
            resp.body = json.dumps({'error': e.message}, ensure_ascii=False)
            resp.status = falcon.HTTP_400

    def on_post(self, req, resp):
        try:
            request_data = json.loads(req.stream.read())
            name = request_data.get("name")
            if not name:
                raise Exception('name canot be null')
            dp_url = request_data.get("dp_url")
            profile_url = request_data.get("profile_url")
            speaker = Speaker(name, dp_url, profile_url).create(self.session)
            resp.body = json.dumps(speaker.as_json(), ensure_ascii=False)
            resp.status = falcon.HTTP_200
        except Exception as e:
            resp.body = json.dumps({'error': e.message}, ensure_ascii=False)
            resp.status = falcon.HTTP_400

    def on_put(self, req, resp, id):
        try:
            request_data = json.loads(req.stream.read())
            speaker = self.session.query(Speaker).filter(Speaker.id == id).first()
            if not speaker:
                resp.body = json.dumps({"status": "speaker not found"}, ensure_ascii=False)
                resp.status = falcon.HTTP_200
                return
            speaker = speaker.update(self.session, request_data)
            resp.body = json.dumps(speaker.as_json(), ensure_ascii=False)
            resp.status = falcon.HTTP_200
        except Exception as e:
            resp.body = json.dumps({'error': e.message}, ensure_ascii=False)
            resp.status = falcon.HTTP_400

    def on_delete(self, req, resp, id):
        try:
            speaker = self.session.query(Speaker).filter(Speaker.id == id).first()
            if not speaker:
                resp.body = json.dumps({"status": "speaker not found"}, ensure_ascii=False)
                resp.status = falcon.HTTP_200
                return
            speaker.delete(self.session)
            resp.body = json.dumps({"status":"speaker deleted sucessfully"}, ensure_ascii=False)
            resp.status = falcon.HTTP_201
        except Exception as e:
            resp.body = json.dumps({'error': e.message}, ensure_ascii=False)
            resp.status = falcon.HTTP_400
