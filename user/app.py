from flask import Flask
from routes.user_routes import exam_routes
import os

app = Flask(__name__)

app.secret_key = os.urandom(24)

# Register routes
app.register_blueprint(exam_routes)

if __name__ == "__main__":
    app.run(debug=True, port=5009)
    