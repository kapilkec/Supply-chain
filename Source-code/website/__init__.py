from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from os import path

db = SQLAlchemy()
DB_NAME = "crud.db"
def create_app():
    app = Flask(__name__)
    app.secret_key="Secret key"
    app.config['SQLALCHEMY_DATABASE_URI'] = "mysql://root:kapil@localhost/crud"
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    db.init_app(app)
    from .views import views
    app.register_blueprint(views, url_prefix='/')
    create_database(app)
    return app

    

def create_database(app):
    if not path.exists('website/' + DB_NAME):
        db.create_all(app=app)
