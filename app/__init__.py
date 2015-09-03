#coding:utf-8
from flask import Flask
from flask.ext.bootstrap import Bootstrap
from flask.ext.sqlalchemy import SQLAlchemy
from config import config
from flask.ext.mail import Mail

bootstrap = Bootstrap()
db = SQLAlchemy()
mail = Mail()

def create_app(config_name):
    app = Flask(__name__)
    
    app.config.from_object(config[config_name])
    config[config_name].init_app(app)

    mail.init_app(app)
    bootstrap.init_app(app)  
    db.init_app(app)
    
    #app入口处
    from .main import main as main_blueprint
    app.register_blueprint(main_blueprint)
    
    from .auth import auth as auth_blueprint
    app.register_blueprint(auth_blueprint, url_prefix='/auth')

    app.debug = True
    return app
