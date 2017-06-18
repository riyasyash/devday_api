class DBHelper:

    def create(self,object, session):
        try:
            session.add(object)
            session.commit()
            return object
        except Exception as e:
            raise Exception(e.message)

    def update(self,object, session, update_hash):
        try:
            for key,value in update_hash.items():
                setattr(object,key,value)
            session.add(object)
            session.commit()
            return object
        except Exception as e:
            raise Exception(e.message)

    def delete(self, object, session):
        try:
            session.delete(object)
            session.commit()
        except Exception as e:
            raise Exception(e.message)