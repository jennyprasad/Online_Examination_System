from flask import jsonify, request
from services.live_session_service import ExaminationService

def to_dict(obj):
    return {column.name: getattr(obj, column.name) for column in obj.__table__.columns}


class ExaminationController:
    def __init__(self):  # Corrected to __init__
        self.service = ExaminationService()  # Initialize the service here

    # LiveSession Routes
    def get_live_session(self, session_id):
        live_session = self.service.get_live_session(session_id)
        if live_session:
            return jsonify(to_dict(live_session))
        return jsonify({"error": "Live session not found"}), 404

    def create_live_session(self):
        live_session_data = request.json
        new_live_session = self.service.create_live_session(live_session_data)
        return jsonify(to_dict(new_live_session)), 201

    def update_live_session(self, session_id):
        live_session_data = request.json
        updated_live_session = self.service.update_live_session(session_id, live_session_data)
        if updated_live_session:
            return jsonify(to_dict(updated_live_session))
        return jsonify({"error": "Live session not found"}), 404

    def delete_live_session(self, session_id):
        deleted_live_session = self.service.delete_live_session(session_id)
        if deleted_live_session:
            return jsonify(to_dict(deleted_live_session))
        return jsonify({"error": "Live session not found"}), 404


    def get_all_live_session(self):
        live_sessions=self.service.get_all_live_session()
        if live_sessions:
            return [to_dict(live_session) for live_session in live_sessions]  
        else:
            return {"error": "No Live session found"}