from flask import jsonify, request
from services.qp_service import QuestionService


def to_dict(obj):
      return {column.name: getattr(obj, column.name) for column in obj.__table__.columns}

class QuestionController:
    def __init__(self):
        self.service = QuestionService()
        

    # QuestionPaper-related endpoints
    def get_question_paper(self, question_paper_id):
        question_paper = self.service.get_question_paper(question_paper_id)
        return jsonify(to_dict(question_paper)) if question_paper else jsonify({"error": "QuestionPaper not found"}), 404
    
    
    def get_all_question_papers(self):
        question_papers = self.service.get_all_question_paper()
        if question_papers:
            return [to_dict(question_paper) for question_paper in question_papers]  
        else:
            return {"error": "No Question Paper found"}

    def create_question_paper(self):
        question_paper_data = request.get_json()
        question_paper = self.service.create_question_paper(question_paper_data)
        return jsonify(to_dict(question_paper)), 201
    
    def get_question_paper_with_questions(self, question_paper_id):
        question_paper_data = self.service.get_question_paper_with_questions(question_paper_id)

        # Check if there's an error in the data
        if "error" in question_paper_data:
            return {"error": question_paper_data["error"]}, 404

        return question_paper_data, 200
    

    # Question-related endpoints
    def get_question(self, question_id):
        question = self.service.get_question(question_id)
        return jsonify(to_dict(question)) if question else jsonify({"error": "Question not found"}), 404

    def create_question(self):
        question_data = request.get_json()
        question = self.service.create_question(question_data)
        return jsonify(to_dict(question)), 201

    # Option-related endpoints
    def get_option(self, option_id):
        option = self.service.get_option(option_id)
        return jsonify(to_dict(option)) if option else jsonify({"error": "Option not found"}), 404

    def create_option(self):
        option_data = request.get_json()
        option = self.service.create_option(option_data)
        return jsonify(to_dict(option)), 201

    # CorrectAnswer-related endpoints
    def get_correct_answer(self, correct_answer_id):
        correct_answer = self.service.get_correct_answer(correct_answer_id)
        return jsonify(to_dict(correct_answer)) if correct_answer else jsonify({"error": "CorrectAnswer not found"}), 404

    def create_correct_answer(self):
        correct_answer_data = request.get_json()
        correct_answer = self.service.create_correct_answer(correct_answer_data)
        return jsonify(to_dict(correct_answer)), 201
