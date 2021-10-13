import logging
import os

from app import flask

APP = flask.create_app()

if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO)
    logging.info("Starting API...")
    APP.run(
        host="0.0.0.0",
        port=os.environ.get("PORT", 8080),
        debug=True,
        use_reloader=True,
    )
