from flask import Flask
from flask_cors import CORS
from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy
import logging

from static.logger_config import custom_logger



db = SQLAlchemy()
migrate = Migrate()

logger = logging.getLogger('static')
logger = custom_logger(logger)
cors = CORS()


def application(test_config=None):
    app = Flask(__name__)
    app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://jnrfayqoucvzrz:ddc3d1a76fdb74ca23049c8b0cb87c97a642069c6f8d4c0666ddfd1eafc418b9@ec2-18-214-134-226.compute-1.amazonaws.com:5432/db3tsq49632rms'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    from static.todoApp.model.todo_list_model import Todo
    db.init_app(app)
    migrate.init_app(app, db)
    cors.init_app(app,resource={r"/api/*": {"origins": "*"}})

    from static.todoApp import todo_list
    app.register_blueprint(todo_list,url_prefix = "/api/v1")

    return app