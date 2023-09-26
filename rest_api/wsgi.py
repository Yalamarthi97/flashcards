from app import app
import os
import logging
from flask import url_for


@app.route("/", methods=["GET"])
def health_check():
    logging.warning("    works perfectly      ")
    return "Working Perfectly!!", 200


if __name__ == "__main__":
    app.run(host="0.0.0.0", debug=True, port=os.getenv("PORT", 5000))
