from flask import Blueprint,request,render_template
from controller.eval_controller import EvaluationController


eval_routes = Blueprint('eval_routes', __name__)
controller = EvaluationController()


#route to get evaluation by evaluation_id
@eval_routes.route("/evaluation/<int:evaluation_id>", methods=["GET"])
def get_eval(evaluation_id):
    # Fetch evaluation data using the controller
    result = controller.get_eval(evaluation_id)
        # Pass the evaluation data to the view_result template
    return render_template("view_result.html", evaluation=result)

#route to create a new evaluation
@eval_routes.route("/evaluation", methods=["POST"])
def create_eval():
    evaluation_data=request.json
    return controller.create_eval(evaluation_data)

#route to update the evaluation by evaluation_id
@eval_routes.route("/evaluations/<int:evaluation_id>", methods=["PUT"])
def update_evaluation(evaluation_id):
    update_data = request.json
    return controller.update_evaluation(evaluation_id, update_data)


#route to delete the evaluation by evaluation_id
@eval_routes.route("/evaluations/<int:evaluation_id>", methods=["DELETE"])
def delete_evaluation(evaluation_id):
    return controller.delete_evaluation(evaluation_id)




@eval_routes.route('/student_portal')
def student_portal():
    return render_template('student_portal.html')
