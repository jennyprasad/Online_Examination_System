from flask import Blueprint, request,render_template
from controllers.live_session_controller import ExaminationController

# Create the blueprint
exam_routes = Blueprint('exam_routes', __name__)

# Instantiate the controller
examination_controller = ExaminationController()

# Define routes using the blueprint
@exam_routes.route('/live_sessions/<int:session_id>', methods=['GET'])
def get_live_session(session_id):
    return examination_controller.get_live_session(session_id)

@exam_routes.route('/live_sessions', methods=['POST'])
def create_live_session():
    return examination_controller.create_live_session()

@exam_routes.route('/live_sessions/<int:session_id>', methods=['PUT'])
def update_live_session(session_id):
    return examination_controller.update_live_session(session_id)

@exam_routes.route('/live_sessions/<int:session_id>', methods=['DELETE'])
def delete_live_session(session_id):
    return examination_controller.delete_live_session(session_id)


@exam_routes.route("/live_sessions", methods=["GET"])
def get_all_live_session():
    live_sessions = examination_controller.get_all_live_session()
    
    if isinstance(live_sessions, dict) and live_sessions.get("error"):

        return render_template("view_all_live_sessions.html", error=live_sessions.get("error"))
    
    return render_template("view_all_live_sessions.html", live_sessions=live_sessions)


@exam_routes.route("/admin_portal", methods=["GET"])
def admin_portal():
    return render_template("admin_portal.html")
