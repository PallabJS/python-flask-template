import os
from flask import Flask
from wazirx_api.extensions.initialization import install_blueprints


import config


# Initialize flask app
app = Flask(__name__)


@app.route("/", methods=["GET"])
def base_route():
    return {"status": "ok"}


if __name__ == "__main__":

    # Install Blueprints
    install_blueprints(app)

    if config.env == "production":
        app.run(host="0.0.0.0", port=os.getenv("PORT"))
    else:
        app.run(port=8000, debug=True, threaded=True)
