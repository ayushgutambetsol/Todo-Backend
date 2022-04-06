# from flask import Flask
# from flask_migrate import Migrate
# from flask_sqlalchemy import SQLAlchemy
# import logging

# from static.logger_config import custom_logger


# db = SQLAlchemy()
# migrate = Migrate()

# logger = logging.getLogger('static')
# logger = custom_logger(logger)


# def create_app(test_config=None):
#     app = Flask(__name__)
#     app.config['SQLALCHEMY_DATABASE_URI'] = 'postgres://maepgdupzvcqru:2de24244b6ca685cd41dc98ae29c30c448ded6a6bcb0ff02afbd66dd5a35730f@ec2-52-73-155-171.compute-1.amazonaws.com:5432/dbmevkl5rhd3tg'
#     app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

#     from static.todoApp.model.todo_list_model import Todo
#     db.init_app(app)
#     migrate.init_app(app, db)

#     from static.todoApp import todo_list
#     app.register_blueprint(todo_list, url_prefix="/api/v1")

#     return app


from flask import Flask, render_template, request, redirect, url_for, jsonify
from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy


# Creating a Flask App
app = Flask(__name__)


# Connecting the Database
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgres://maepgdupzvcqru:2de24244b6ca685cd41dc98ae29c30c448ded6a6bcb0ff02afbd66dd5a35730f@ec2-52-73-155-171.compute-1.amazonaws.com:5432/dbmevkl5rhd3tg'         
db = SQLAlchemy(app)
migrate = Migrate(app, db)


# # Creating a Model
class Todo(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100))
    complete = db.Column(db.Boolean, default=False)
    date_modified = db.Column(db.DateTime, default=db.func.current_timestamp())


# Default Hello World
@app.route("/")
def home():
    return "hello world"


if __name__ == "__main__":
    app.run(debug=True)