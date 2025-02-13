from flask import jsonify, request
from services.examination_services import ExaminationService


def to_dict(obj):
    return {column.name: getattr(obj, column.name) for column in obj.__table__.columns}

class ExaminationController:
    def __init__(self):
        self.service = ExaminationService()

    # Examination 
    def get_examination(self, exam_id):
        examination = self.service.get_examination(exam_id)
        print(to_dict(examination))
    
        return (to_dict(examination)) if examination else{"error":"examination not found"}
    
    
    def get_all_examinations(self):
        examinations = self.service.get_all_examinations()
        if examinations:
            return [to_dict(examination) for examination in examinations]  
        else:
            return {"error": "No examinations found"}
    
    
    

    def create_examination(self):
        examination_data = request.json
        new_examination = self.service.create_examination(examination_data)
        return jsonify(to_dict(new_examination)), 201

    def update_examination(self, exam_id):
        examination_data = request.json
        updated_examination = self.service.update_examiantion(exam_id, examination_data)
        if updated_examination:
            return jsonify(to_dict(updated_examination))
        return jsonify({"error": "Examination not found"}), 404

    def delete_examination(self, exam_id):
        deleted_examination = self.service.delete_examiantion(exam_id)
        if deleted_examination:
            return jsonify(to_dict(deleted_examination))
        return jsonify({"error": "Examination not found"}), 404

    # UserResponse Routes
    def get_user_response(self, response_id):
        user_response = self.service.get_UserResponse(response_id)
        if user_response:
            return jsonify(to_dict(user_response))
        return jsonify({"error": "User response not found"}), 404

    def create_user_response(self):
        user_response_data = request.json
        new_user_response = self.service.create_UserResponse(user_response_data)
        return jsonify(to_dict(new_user_response)), 201

    def update_user_response(self, response_id):
        user_response_data = request.json
        updated_user_response = self.service.update_UserResponse(response_id, user_response_data)
        if updated_user_response:
            return jsonify(to_dict(updated_user_response))
        return jsonify({"error": "User response not found"}), 404

    def delete_user_response(self, response_id):
        deleted_user_response = self.service.delete_UserResponse(response_id)
        if deleted_user_response:
            return jsonify(to_dict(deleted_user_response))
        return jsonify({"error": "User response not found"}), 404

