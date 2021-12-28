# This file is intended to install all extensions, blueprints, databases, etc...

from core.api import app_blueprints


def initialize_app(app):
    # Blueprints(routes)
    for blueprint in app_blueprints:
        app.register_blueprint(blueprint)
