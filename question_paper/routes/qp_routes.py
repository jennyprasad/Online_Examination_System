from flask import Blueprint, request,render_template
from controllers.qp_controllers import QuestionController

question_routes = Blueprint('question_routes', __name__)
controller = QuestionController()

# QuestionPaper routes
@question_routes.route("/question_paper/<int:question_paper_id>", methods=["GET"])
def get_question_paper(question_paper_id):
    return controller.get_question_paper(question_paper_id)

@question_routes.route("/question_paper",methods=["GET"])
def get_all_question_papers():
    question_papers= controller.get_all_question_papers()
    if isinstance(question_papers, dict) and question_papers.get("error"):

        return render_template("view_all_question_papers.html", error=question_papers.get("error"))
    
    return render_template("view_all_question_papers.html", question_papers=question_papers)




@question_routes.route("/admin_portal")
def admin_portal():
    return render_template('admin_portal.html')



@question_routes.route("/question_paper", methods=["POST"])
def create_question_paper():
    question_paper_data = request.json
    return controller.create_question_paper()


@question_routes.route("/question_paper/<int:question_paper_id>/with_questions", methods=["GET"])
def get_question_paper_with_questions(question_paper_id):
    # Use the instance method to get the data
    question_paper_data, status_code = controller.get_question_paper_with_questions(question_paper_id)
    
    if status_code != 200:
        return render_template('error.html', error_message=question_paper_data["error"]), status_code

    # Pass the fetched data to the template
    return render_template('view_question_paper_with_questions.html', question_paper=question_paper_data)



# Question routes
@question_routes.route("/question/<int:question_id>", methods=["GET"])
def get_question(question_id):
    return controller.get_question(question_id)

@question_routes.route("/question", methods=["POST"])
def create_question():
    question_data = request.json
    return controller.create_question()

# Option routes
@question_routes.route("/option/<int:option_id>", methods=["GET"])
def get_option(option_id):
    return controller.get_option(option_id)

@question_routes.route("/option", methods=["POST"])
def create_option():
    option_data = request.json
    return controller.create_option()

# CorrectAnswer routes
@question_routes.route("/correct_answer/<int:correct_answer_id>", methods=["GET"])
def get_correct_answer(correct_answer_id):
    return controller.get_correct_answer(correct_answer_id)

@question_routes.route("/correct_answer", methods=["POST"])
def create_correct_answer():
    correct_answer_data = request.json
    return controller.create_correct_answer()
