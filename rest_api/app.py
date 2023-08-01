import os

from flask import Flask
from flask_cors import CORS


def create_app():
    app = Flask(__name__)

    # TODO: Gotta remove this when moving to prod maybe
    CORS(app)

    app.secret_key = os.environ.get("FLASK_APP_SECRET", "hello")
    app.config["DEBUG"] = True

    app.app_context().push()
    return app


app = create_app()
