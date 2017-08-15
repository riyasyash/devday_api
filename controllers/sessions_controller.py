import json
import os
import sys

import falcon

sys.path.append(os.path.dirname(os.path.abspath(__file__)) + "/..")
from models.session import Session


class SessionsController():
    def on_get(self, req, resp, id=None):
        try:
            if not id:
                sessions = self.session.query(Session).all()
                resp.body = json.dumps([session.as_json() for session in sessions], ensure_ascii=False)
            else:
                session = self.session.query(Session).filter(Session.id == id).first()
                if not session:
                    resp.body = json.dumps({"status":"session not found"}, ensure_ascii=False)
                    resp.status = falcon.HTTP_404
                    return
                resp.body = json.dumps(session.as_json(), ensure_ascii=False)
            resp.status = falcon.HTTP_200
        except Exception as e:
            resp.body = json.dumps({'error': e.message}, ensure_ascii=False)
            resp.status = falcon.HTTP_400

    def on_post(self, req, resp):
        try:
            request_data = json.loads(req.stream.read())
            topic = request_data.get("topic")
            if not topic:
                raise Exception('topic canot be null')
            description = request_data.get("description")
            session = Session(topic, description).create(self.session)
            resp.body = json.dumps(session.as_json(), ensure_ascii=False)
            resp.status = falcon.HTTP_200
        except Exception as e:
            resp.body = json.dumps({'error': e.message}, ensure_ascii=False)
            resp.status = falcon.HTTP_400

    def on_put(self, req, resp, id):
        try:
            request_data = json.loads(req.stream.read())
            session = self.session.query(Session).filter(Session.id == id).first()
            if not session:
                resp.body = json.dumps({"status": "session not found"}, ensure_ascii=False)
                resp.status = falcon.HTTP_404
                return
            session = session.update(self.session, request_data)
            resp.body = json.dumps(session.as_json(), ensure_ascii=False)
            resp.status = falcon.HTTP_200
        except Exception as e:
            resp.body = json.dumps({'error': e.message}, ensure_ascii=False)
            resp.status = falcon.HTTP_400

    def on_delete(self, req, resp, id):
        try:
            session = self.session.query(Session).filter(Session.id == id).first()
            if not session:
                resp.body = json.dumps({"status": "session not found"}, ensure_ascii=False)
                resp.status = falcon.HTTP_200
                return
            session.delete(self.session)
            resp.body = json.dumps({"status":"session deleted sucessfully"}, ensure_ascii=False)
            resp.status = falcon.HTTP_201
        except Exception as e:
            resp.body = json.dumps({'error': e.message}, ensure_ascii=False)
            resp.status = falcon.HTTP_400
