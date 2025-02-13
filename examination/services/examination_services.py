from models.examination_model import SessionLocal,Examination,UserResponse,Question,Option,QuestionPaper,CorrectAnswer


class ExaminationService:
    def __init__(self):
        self.db=SessionLocal()

# examination

    def get_examination(self,exam_id):
        return self.db.query(Examination).filter(Examination.exam_id==exam_id).first()
    
    
    def get_all_examinations(self):
        return self.db.query(Examination).all()
    
    
    def create_examination(self,examination_data):
        examination=Examination(**examination_data)
        self.db.add(examination)
        self.db.commit()
        return examination
    
    def update_examiantion(self,exam_id,examination_data):
     examination=self.get_examination(exam_id)
     if examination:
        for key,value in examination_data.items():
          setattr(examination,key,value)
        self.db.commit()
        return examination
            
    def delete_examiantion(self,exam_id):
        examination=self.get_examination(exam_id)
        if examination:
            self.db.delete(examination)
            self.db.commit()
            return examination
        
        
        
# user response

    def get_UserResponse(self,response_id):
        return self.db.query(UserResponse).filter(UserResponse.response_id==response_id).first()
    
    def create_UserResponse(self,UserResponse_data):
        userresponse=UserResponse(**UserResponse_data)
        self.db.add(userresponse)
        self.db.commit()
        return userresponse
    
    def update_UserResponse(self,response_id,UserResponse_data):
     userresponse=self.get_UserResponse(response_id)
     if userresponse:
        for key,value in UserResponse_data.items():
            setattr(userresponse,key,value)
        self.db.commit()
        return userresponse
            
    def delete_UserResponse(self,response_id):
        userresponse=self.get_UserResponse(response_id)
        if userresponse:
            self.db.delete(userresponse)
            self.db.commit()
            return userresponse

