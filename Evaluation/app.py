from flask import Flask
from routes.eval_routes import eval_routes

app = Flask(__name__)

# Register routes
app.register_blueprint(eval_routes)

if __name__ == "__main__":
    app.run(debug=True, port=5008)     