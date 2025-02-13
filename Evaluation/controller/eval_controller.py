from flask import jsonify,request
from services.eval_service import EvalService

def to_dict(obj):
    return {column.name: getattr(obj, column.name) for column in obj.__table__.columns}

class EvaluationController:
    def __init__(self):
        self.service = EvalService()
        
        
    def get_eval(self,evaluation_id):
        evaluation = self.service.get_eval(evaluation_id)
        return jsonify(to_dict(evaluation)) if evaluation else jsonify({"error": "Evaluation not found"}),404
    
    def create_eval(self,Evaluation_data):
        evaluation = self.service.create_eval(Evaluation_data)
        return jsonify(to_dict(evaluation)),201
        
    
        
    def update_eval(self,evaluation_id,update_data):
        update_data = request.get_json()
        evaluation = self.service.update_eval(evaluation_id,update_data)
        return jsonify(to_dict(evaluation)) if evaluation else jsonify({"error": "Evaluation not found"}), 404
    
        
    def calculate_score_with_respect_to_max(self,score):
        evaluation = self.service.calculate_score_with_respect_to_max(score)
        return jsonify(to_dict(evaluation)) if evaluation else jsonify({"error": "Evaluation not found"}), 404
        
        
    def delete_evaluation(self,evaluation_id):
        evaluation = self.service.delete_evaluation(evaluation_id)
        return jsonify(to_dict(evaluation)) if evaluation else jsonify({"error": "Evaluation not found"}), 404
    