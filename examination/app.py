from flask import Flask
from routes.examination_routes import examination_routes

app=Flask(__name__)

app.register_blueprint(examination_routes)

if __name__=="__main__":
    app.run(debug=True,port=5011)

