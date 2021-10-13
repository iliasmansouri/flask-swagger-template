from app import core


def say_hello():
    return {"message": "Hello API!"}


def process_image(payload):
    return core.process_image(payload)


def process_audio(payload):
    return core.process_audio(payload)


def process_text(payload):
    return core.process_text(payload)
