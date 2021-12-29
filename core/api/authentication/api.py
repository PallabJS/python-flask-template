from os import readlink
from flask import Blueprint, request

from core.templates.Response import Response
from app_utils import log, mdb
from core.utility.Auth.Auth import Auth


from core.api.decorators.auth import requires_login


auth_api = Blueprint("auth", __name__)

auth = Auth()


@auth_api.route("/signup", methods=["post"])
def signup():
    res = Response()
    return res.json()


@auth_api.route("/login", methods=["get", "post"])
@requires_login
def login():
    res = Response()
    return res.json()
