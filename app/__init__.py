# app/__init__.py

from flask import Flask

def create_app():
    app = Flask(__name__, instance_relative_config=True)
    app.config.from_object('config')
    from app import catalogo, client_secrets, crud, database
    return app
