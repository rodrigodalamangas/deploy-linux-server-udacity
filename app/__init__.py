# app/__init__.py

from flask import Flask

def create_app():
    from app import catalogo
    app.config.from_object('config')
    return app
