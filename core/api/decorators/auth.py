from flask import request
from functools import wraps


def requires_login(handler):
    @wraps(handler)
    def pre_handler(*args, **kwargs):
        if request.method == "GET":
            return handler(*args, **kwargs)
        else:
            return "unauthorized"
    return pre_handler
