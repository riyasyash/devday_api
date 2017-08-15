import json
import os
import sys

import falcon

sys.path.append(os.path.dirname(os.path.abspath(__file__)) + "/..")
from models.location import Location


class LocationsController():
    def on_get(self, req, resp, id=None):
        try:
            if not id:
                locations = self.session.query(Location).all()
                resp.body = json.dumps([location.as_json() for location in locations], ensure_ascii=False)
            else:
                location = self.session.query(Location).filter(Location.id == id).first()
                if not location:
                    resp.body = json.dumps({"status":"location not found"}, ensure_ascii=False)
                    resp.status = falcon.HTTP_404
                    return
                resp.body = json.dumps(location.as_json(), ensure_ascii=False)
            resp.status = falcon.HTTP_200
        except Exception as e:
            resp.body = json.dumps({'error': e.message}, ensure_ascii=False)
            resp.status = falcon.HTTP_400

    def on_post(self, req, resp):
        try:
            request_data = json.loads(req.stream.read())
            place = request_data.get("place")
            if not place:
                raise Exception('place canot be null')
            location_url = request_data.get("location_url")
            location = Location(place, location_url).create(self.session)
            resp.body = json.dumps(location.as_json(), ensure_ascii=False)
            resp.status = falcon.HTTP_201
        except Exception as e:
            resp.body = json.dumps({'error': e.message}, ensure_ascii=False)
            resp.status = falcon.HTTP_400

    def on_put(self, req, resp, id):
        try:
            request_data = json.loads(req.stream.read())
            location = self.session.query(Location).filter(Location.id == id).first()
            if not location:
                resp.body = json.dumps({"status": "location not found"}, ensure_ascii=False)
                resp.status = falcon.HTTP_404
                return
            location = location.update(self.session, request_data)
            resp.body = json.dumps(location.as_json(), ensure_ascii=False)
            resp.status = falcon.HTTP_200
        except Exception as e:
            resp.body = json.dumps({'error': e.message}, ensure_ascii=False)
            resp.status = falcon.HTTP_400

    def on_delete(self, req, resp, id):
        try:
            location = self.session.query(Location).filter(Location.id == id).first()
            if not location:
                resp.body = json.dumps({"status": "location not found"}, ensure_ascii=False)
                resp.status = falcon.HTTP_404
                return
            location = location.delete(self.session)
            resp.body = json.dumps({"status":"location deleted succesfully"}, ensure_ascii=False)
            resp.status = falcon.HTTP_201
        except Exception as e:
            resp.body = json.dumps({'error': e.message}, ensure_ascii=False)
            resp.status = falcon.HTTP_400
