from flask import Flask
from routes.qp_routes import question_routes

app = Flask(__name__)

# Register routes
app.register_blueprint(question_routes)

if __name__ == "__main__":
    app.run(debug=True, port=5010)
