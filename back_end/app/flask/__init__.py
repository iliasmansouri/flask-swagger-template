import config
import connexion
from app.flask import error_handler
from flask_cors import CORS
from swagger_ui_bundle import swagger_ui_path


def create_app():
    options = {"swagger_path": swagger_ui_path}

    app = connexion.App(
        __name__, specification_dir=config.SPECIFICATION_DIR, options=options
    )
    CORS(app.app)
    app.add_api("swagger.yaml", strict_validation=True, validate_responses=True)
    error_handler.register_error_handlers(app)
    return app


def dummy_api_key_validation(*_args, **_kwargs):
    """Dummy function for Connexion API key validation."""
    return {}
