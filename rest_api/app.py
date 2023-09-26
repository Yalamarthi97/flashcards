import os

from flask import Flask
from flask_cors import CORS

from handler.cards.urls import card_urls_v1
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate, upgrade

db = SQLAlchemy()


def create_app():
    app = Flask(__name__)

    # TODO: Gotta remove this when moving to prod maybe
    CORS(app)
    db.init_app(app)
    Migrate(app, db)
    upgrade("migrations")
    app.secret_key = os.environ.get("FLASK_APP_SECRET", "hello")
    app.config.from_pyfile("config.py")

    card_urls_v1(app, prefix="v1")

    app.app_context().push()
    return app


app = create_app()
