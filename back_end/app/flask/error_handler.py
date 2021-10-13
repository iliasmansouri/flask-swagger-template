from flask import jsonify


def handle_not_implemented(_):
    response = jsonify({"Error message": "Not Implemented"})
    response.status_code = 501
    return response


def handle_not_found(error):
    response = jsonify({"Error message": error.message})
    response.status_code = 404
    return response


def register_error_handlers(app):
    app.add_error_handler(NotImplementedError, handle_not_implemented)
