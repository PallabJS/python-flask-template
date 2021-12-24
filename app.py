import os
from flask import Flask
from wazirx_api.extensions.initialization import install_blueprints


# Initialize flask app
app = Flask(__name__)


@app.route("/", methods=["GET"])
def base_route():
    return {"status": "ok"}


if __name__ == "__main__":

    # Install Blueprints
    install_blueprints(app)
    print("BLUEPRINTS INSTALLED")

    print("OS PORT->", os.getenv("PORT"))

    # Start Flask Server
    app.run(host="0.0.0.0", port=os.getenv("PORT"))
