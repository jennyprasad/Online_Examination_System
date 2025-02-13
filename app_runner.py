import subprocess

# Run the service corresponding to the user_app
def run_user_service():
    subprocess.Popen([r"C:\Users\khush\OneDrive\Desktop\online_exam\venv\Scripts\python.exe", "user/app.py"])

# Run the service corresponding to the question_paper_app
def run_question_paper_service():
    subprocess.Popen([r"C:\Users\khush\OneDrive\Desktop\online_exam\venv\Scripts\python.exe", "question_paper/app.py"])

def run_examination_service():
    subprocess.Popen([r"C:\Users\khush\OneDrive\Desktop\online_exam\venv\Scripts\python.exe","examination/app.py"])
    
def run_evaluation_service():
    subprocess.Popen([r"C:\Users\khush\OneDrive\Desktop\online_exam\venv\Scripts\python.exe","Evaluation/app.py"])
    
def run_Live_session_app_service():
     subprocess.Popen([r"C:\Users\khush\OneDrive\Desktop\online_exam\venv\Scripts\python.exe","Live_session_app/app.py"])
        

if __name__ == '__main__':
    # Start each service
    run_user_service()
    run_question_paper_service()
    run_examination_service()
    run_evaluation_service()
    run_Live_session_app_service()

    # Keep the main process running, and handle KeyboardInterrupt for graceful termination
    try:
        while True:
            pass
    except KeyboardInterrupt:
        print("\nTerminating all processes. Goodbye!")
