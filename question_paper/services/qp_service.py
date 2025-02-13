from models.qp_model import SessionLocal, QuestionPaper, Question, CorrectAnswer, Option

class QuestionService:
    def __init__(self):
        self.db = SessionLocal()

    def get_question_paper(self, question_paper_id):
        return self.db.query(QuestionPaper).filter(QuestionPaper.question_paper_id == question_paper_id).first()
    
    def get_all_question_paper(self):
        return self.db.query(QuestionPaper).all()

    def create_question_paper(self, question_paper_data):
        question_paper = QuestionPaper(**question_paper_data)
        self.db.add(question_paper)
        self.db.commit()
        return question_paper
    
    def get_question_paper_with_questions(self, question_paper_id):
        try:
            # Fetch the question paper
            question_paper = self.db.query(QuestionPaper).filter(QuestionPaper.question_paper_id == question_paper_id).first()
            if not question_paper:
                return {"error": "Question paper not found"}

            # Prepare response structure
            question_paper_data = {
                "question_paper_id": question_paper.question_paper_id,
                "title": question_paper.question_paper_title,
                "metadata": question_paper.question_paper_meta_data,
                "min_req_questions": question_paper.min_req_number_of_questions_to_be_attempted,
                "max_attemptable_questions": question_paper.max_number_of_questions_that_can_be_attempted,
                "max_score": question_paper.max_score,
                "questions": []
            }

            # Fetch associated questions
            questions = self.db.query(Question).filter(Question.question_paper_id == question_paper_id).all()
            for question in questions:
                question_data = {
                    "question_id": question.question_id,
                    "text": question.question_text,
                    "options": []
                }

                # Fetch options for the question
                options = self.db.query(Option).filter(Option.question_id == question.question_id).all()
                for option in options:
                    question_data["options"].append({
                        "option_id": option.option_id,
                        "text": option.option_text,
                        "label": option.option_label
                    })

                question_paper_data["questions"].append(question_data)

            return question_paper_data

        except Exception as e:
            return {"error": str(e)}
    
    
    

    # Question
    def get_question(self, question_id):
        return self.db.query(Question).filter(Question.question_id == question_id).first()
    

    def create_question(self, question_data):
        question = Question(**question_data)
        self.db.add(question)
        self.db.commit()
        return question

    # Option
    def get_option(self, option_id):
        return self.db.query(Option).filter(Option.option_id == option_id).first()

    def create_option(self, option_data):
        option = Option(**option_data)
        self.db.add(option)
        self.db.commit()
        return option

    # CorrectAnswer
    def get_correct_answer(self, correct_answer_id):
        return self.db.query(CorrectAnswer).filter(CorrectAnswer.question_id == correct_answer_id).first()

    def create_correct_answer(self, correct_answer_data):
        correct_answer = CorrectAnswer(**correct_answer_data)
        self.db.add(correct_answer)
        self.db.commit()
        return correct_answer
