from flask import Blueprint, request,render_template,flash,redirect,url_for,session
from controllers.user_controller import ExamController


exam_routes = Blueprint('exam_routes', __name__)
controller = ExamController()


@exam_routes.route("/user/<int:user_id>", methods=["GET"])
def get_user(user_id):
    return controller.get_user(user_id)

@exam_routes.route("/user",methods=["GET"])
def get_all_users():
    return controller.get_all_users()

@exam_routes.route("/user", methods=["POST"])
def create_user():
    user_data = request.json
    return controller.create_user(user_data)

@exam_routes.route("/user/<int:user_id>", methods=["PUT"])
def update_user(user_id):
    return controller.update_user(user_id)

@exam_routes.route("/user/<int:user_id>", methods=["DELETE"])
def delete_user(user_id):
    return controller.delete_user()

# Student routes
@exam_routes.route("/student/<int:student_id>", methods=["GET"])
def get_student(student_id):
    from_page = request.args.get("from", "student_portal")  # Default to student_portal if not provided
    student = controller.get_student(student_id)  # Fetch the student data

    if student.get("error") is not None:  # Check if the student is not found
        return render_template("view_profile.html", error=student.get("error"), from_page=from_page)

    return render_template("view_profile.html", student=student, from_page=from_page)  # Render profile
    

@exam_routes.route("/student",methods=["GET"])
def get_all_students():
    students= controller.get_all_students()

    if isinstance(students, dict) and students.get("error"):
        return render_template("view_all_students.html", error=students.get("error"))
    
    return render_template("view_all_students.html", students=students) 



@exam_routes.route("/student", methods=["POST"])
def create_student():
    name = request.form.get('name')
    gender = request.form.get('gender')
    date_of_birth = request.form.get('dob')
    address = request.form.get('address')

   
    print(f"Received data: {name}, {gender}, {date_of_birth}, {address}")
    
    student_data = {
        'name': name,
        'gender': gender,
        'date_of_birth': date_of_birth,
        'address': address
    }
    controller.create_student(student_data)
    return render_template("signup.html")

@exam_routes.route("/student/<int:student_id>", methods=["PUT"])
def update_student(student_id):
    return controller.update_student(student_id)

@exam_routes.route("/student/<int:student_id>", methods=["DELETE"])
def delete_student(student_id):
    return controller.delete_student()

@exam_routes.route("/student_portal")
def student_portal():
    email = session.get('email')  # Get the email from session

    if email in student_emails:
        student_id = student_emails.index(email) + 1  # Use the index as a student ID (or another unique ID logic)

        return render_template('student_portal.html', email=email, student_id=student_id)

    
    flash("No student found with this email")
    return redirect(url_for('exam_routes.login'))




@exam_routes.route('/')
def index():
    return render_template('index.html')


student_emails = ['s1p@gmail.com', 's2@gmail.com', 's3@gmail.com', 's4@gmail.com','qps4@gmail.com']
admin_emails = ['admin@gmail.com']


@exam_routes.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        email = request.form.get('email')

        # Check if the email is in the student email list
        if email in student_emails:
            session['email'] = email  # Store the student's email in session
            
            return redirect(url_for('exam_routes.student_portal'))
        
        # Check if the email is an admin email
        elif email in admin_emails:
            # Redirect to admin portal
            return redirect(url_for('exam_routes.admin_portal'))
        
        else:
            flash("Invalid email domain or email not registered.")
            return redirect(url_for('exam_routes.login'))

    return render_template('login.html')


@exam_routes.route("/admin_portal")
def admin_portal():
    return render_template('admin_portal.html')


@exam_routes.route("/signup")
def signup():
    return render_template('signup.html')


@exam_routes.route('/logout')
def logout():
    
    session.clear()
    
    return redirect(url_for('exam_routes.login'))


