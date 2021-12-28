from flask import Blueprint, request

from core.templates.Response import Response


auth_api = Blueprint("auth", __name__)


@auth_api.route("/signup", methods=["post"])
def signup():
    res = Response()


@auth_api.route("/login", methods=["get", "post"])
def login():
    req = request.method

    print(req)

    return ""
