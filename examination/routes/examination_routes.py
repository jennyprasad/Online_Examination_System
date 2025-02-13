from flask import Blueprint,render_template
from controllers.examination_controller import ExaminationController
from models.examination_model import UserResponse,Question,Option

examination_routes = Blueprint('examination_routes', __name__)
controller = ExaminationController()

# Examination routes
@examination_routes.route("/examination/<int:exam_id>", methods=["GET"])
def view_examination(exam_id):
    # Call the controller function to get the examination details
    examination = controller.get_examination(exam_id)
    print("\n,\n", examination)
    # Check if there is an error in the examination data
    if examination.get("error") is not None:
        return render_template("view_examination.html", error=examination.get("error"))
        
    # Render the examination details if no error exists
    return render_template("view_examination.html", examination=[examination],error=None)



@examination_routes.route("/examination", methods=["GET"])
def get_all_examinations():
    examinations = controller.get_all_examinations()
    
    # Check for error in the returned data
    if isinstance(examinations, dict) and examinations.get("error"):
        return render_template("view_all_examinations.html", error=examinations.get("error"))
    
    # Pass the examinations list to the template
    return render_template("view_all_examinations.html", examinations=examinations)

examination_routes.route("/examination", methods=["POST"])(controller.create_examination)
examination_routes.route("/examination/<int:exam_id>", methods=["PUT"])(controller.update_examination)
examination_routes.route("/examination/<int:exam_id>", methods=["DELETE"])(controller.delete_examination)



@examination_routes.route("/student_portal")
def student_portal():
    return render_template('student_portal.html')



@examination_routes.route("/admin_portal")
def admin_portal():
    return render_template('admin_portal.html')


# UserResponse routes
@examination_routes.route("/user_responses/<int:student_user_id>/<int:exam_id>", methods=["GET"])
def get_user_responses(student_user_id, exam_id):
    # Query for all responses for the given student and exam
    user_responses = UserResponse.query.filter_by(student_user_id=student_user_id, exam_id=exam_id).all()

    if not user_responses:
        return render_template("view_examination.html", error="No responses found for this student in this exam")

    response_data_list = []
    for userResponse in user_responses:
        question = Question.query.filter_by(question_id=userResponse.question_id).first()
        options = Option.query.filter_by(question_id=question.question_id).all()
        response_data = {
            "response_id": userResponse.response_id,
            "question": {"id": question.question_id, "text": question.question_text},
            "options": [{"label": opt.option_label, "text": opt.option_text} for opt in options],
            "selected_option_label": userResponse.selected_option_label,
        }
        response_data_list.append(response_data)

    return render_template("view_user_responses.html", responses_data=response_data_list, student_user_id=student_user_id, exam_id=exam_id)

examination_routes.route("/user_response", methods=["POST"])(controller.create_user_response)
examination_routes.route("/user_response/<int:response_id>", methods=["PUT"])(controller.update_user_response)
examination_routes.route("/user_response/<int:response_id>", methods=["DELETE"])(controller.delete_user_response)
