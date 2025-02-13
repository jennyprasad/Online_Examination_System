from models.live_model import SessionLocal, live_session

class ExaminationService:
    def __init__(self):  
        self.db = SessionLocal()

    # LiveSession
    def get_live_session(self, session_id):
        return self.db.query(live_session).filter(live_session.session_id == session_id).first()
    
    
    def get_all_live_session(self):
        return self.db.query(live_session).all()

    def create_live_session(self, live_session_data):
        new_live_session = live_session(**live_session_data)
        self.db.add(new_live_session)
        self.db.commit()
        return new_live_session

    def update_live_session(self, session_id, live_session_data):
        existing_live_session = self.get_live_session(session_id)
        if existing_live_session:
            for key, value in live_session_data.items():
                setattr(existing_live_session, key, value)
            self.db.commit()
            return existing_live_session

    def delete_live_session(self, session_id):
        existing_live_session = self.get_live_session(session_id)
        if existing_live_session:
            self.db.delete(existing_live_session)
            self.db.commit()
            return existing_live_session
