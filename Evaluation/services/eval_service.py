from models.evaluation_model import SessionLocal,Evaluations

class EvalService:
    def __init__(self):
        self.db = SessionLocal()
        
    def get_eval(self,evaluation_id):
         return self.db.query(Evaluations).filter(Evaluations.evaluation_id == evaluation_id).first()
        
    def create_eval(self,Evaluation_data):
         evaluation = Evaluations(**Evaluation_data)
         self.db.add(evaluation)
         self.db.commit()
         return evaluation

         
    def update_eval(self,evaluation_id,update_data):
        evaluation=self.get_eval(evaluation_id)
        if not evaluation:
            return None
        if 'score' in update_data:
            evaluation.score=update_data['score']
            evaluation.score_with_respect_to_max_score = self.calculate_score_with_respect_to_max(evaluation.score)
            self.db.commit()
            return evaluation
        
    def calculate_score_with_respect_to_max(self,score):
        max_score=40
        if score is None:
            return None
        else:
            return(int(score/max_score)*40)
        
    def delete_evaluation(self,evaluation_id):
        evaluation = self.get_evaluation(evaluation_id)
        self.db.delete(evaluation)
        self.db.commit()
        
    
    def close(self):
        self.db.close()
    
            
          

        
        
    
            
