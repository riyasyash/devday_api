import json
import os
import sys

import falcon

sys.path.append(os.path.dirname(os.path.abspath(__file__)) + "/..")
from models.event import Event


class EventsController():
    def on_get(self, req, resp, id=None):
        try:
            if id:
                event = self.session.query(Event).filter(Event.id == id).first()
                resp.body = json.dumps(event.as_json(), ensure_ascii=False)
            else:
                events = self.session.query(Event).all()
                resp.body = json.dumps([event.as_json() for event in events], ensure_ascii=False)
            resp.status = falcon.HTTP_200
        except Exception as e:
            resp.body = json.dumps({'error': e.message}, ensure_ascii=False)
            resp.status = falcon.HTTP_400

    def on_post(self, req, resp):
        try:
            request_data = json.loads(req.stream.read())
            location_id = request_data.get("location_id")
            if not location_id:
                raise Exception('place canot be null')
            meetup_link = request_data.get("meetup_link")
            title = request_data.get('title')
            description = request_data.get('description')
            event = Event(title=title, fk_location_id=location_id, meetup_link=meetup_link, description=description).create(self.session)
            resp.body = json.dumps(event.as_json(), ensure_ascii=False)
            resp.status = falcon.HTTP_200
        except Exception as e:
            resp.body = json.dumps({'error': e.message}, ensure_ascii=False)
            resp.status = falcon.HTTP_400

    def on_put(self, req, resp, id):
        try:
            request_data = json.loads(req.stream.read())
            event = self.session.query(Event).filter(Event.id == id).first()
            event = event.update(self.session, request_data)
            resp.body = json.dumps(event.as_json(), ensure_ascii=False)
            resp.status = falcon.HTTP_200
        except Exception as e:
            resp.body = json.dumps({'error': e.message}, ensure_ascii=False)
            resp.status = falcon.HTTP_400

