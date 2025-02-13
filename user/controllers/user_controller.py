from flask import jsonify,request
from services.user_services import ExamService

def to_dict(obj):
    return {column.name: getattr(obj, column.name) for column in obj.__table__.columns}

class ExamController:
    def __init__(self):
        self.service = ExamService()
        
    
    def get_all_users(self):
     users = self.service.get_all_users()  # Fetch all users (likely a list of SQLAlchemy objects)
     if users:
        # Convert each user to a dictionary and return the list
        return jsonify([to_dict(u) for u in users])  # Return a list of user dictionaries as JSON
     else:
        return jsonify({"error": "No users found"})  # Return an error if no users are found

        

    def get_user(self, user_id):
        user = self.service.get_user(user_id)
        return jsonify(to_dict(user)) if user else jsonify({"error": "User not found"})

    def create_user(self, user_data):
        user = self.service.create_user(user_data)
        return jsonify(to_dict(user))
    
    
    def update_user(self,user_id):
        user_data=request.json
        updated_user=self.update_user(user_id,user_data)
        return jsonify(to_dict(updated_user))if updated_user else jsonify({"error": "User not found"})
    
    
    def delete_user(self,user_id):
        deleted_user=self.service.delete_user(user_id)
        return jsonify({"message":"User deleted"})if deleted_user else jsonify({"error":"User not found"})


#student
    def get_student(self, student_id):
        student = self.service.get_student(student_id)
        print(to_dict(student))
        
        
        return to_dict(student) if student else {"error": "Student not found"}
        # return jsonify(to_dict(student)) if student else jsonify({"error": "Student not found"})
        
        
    def get_all_students(self):
        students=self.service.get_all_students()
        if students:
            # Convert each student object to a dictionary
            return [to_dict(student) for student in students]  # Return list of student dictionaries
        else:
            return {"error": "No students found"}    
        
        
       
    def create_student(self, student_data):
        student = self.service.create_student(student_data)
        return jsonify(to_dict(student))
    
    def update_student(self,student_id):
        student_data=request.json
        updated_student=self.update_student(student_id,student_data)
        return jsonify(to_dict(updated_student))if updated_student else jsonify({"error": "Student not found"})
    
    def delete_student(self,student_id):
        deleted_student=self.service.delete_student(student_id)
        return jsonify({"message":"Student deleted"})if deleted_student else jsonify({"error":"Student not found"})
