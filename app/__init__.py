# app/__init__.py

from flask import Flask

def create_app():
    app = Flask(__name__, instance_relative_config=True)
    from catalogo import app as app_blueprint
    app.register_blueprint(app_blueprint)
    app.config.from_object('config')
    return app
