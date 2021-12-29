# This file is intended to install all extensions, blueprints, databases, etc...
import config

# Service access variables
log = None
mdb = None
bcrypt = None
jwt = None


def initialize_app(app):
    # Global variables
    global log
    global mdb
    global bcrypt
    global jwt

    """ *Import All independent services first then the dependant ones """

    # Initialize loggger
    from core.extensions.Logger import AppLogger
    log = AppLogger()

    # MongoDB
    from core.extensions.Mongo import MongoConnector
    mdb = MongoConnector(config.mongo_uri, "test")

    # Flask Bcrypt
    from flask_bcrypt import Bcrypt
    bcrypt = Bcrypt(app)

    # Jwt
    import jwt as pyjwt
    jwt = pyjwt

    # Blueprints(routes)
    from core.api import app_blueprints
    for blueprint in app_blueprints:
        app.register_blueprint(blueprint)
