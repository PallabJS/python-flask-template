from flask import Flask
from wazirx_api.extensions.initialization import install_blueprints


# Initialize flask app
app = Flask(__name__)


@app.route("/", methods=["GET"])
def base_route():
    return {"status": "ok"}


# App intance entry point
def start_flask_app():
    # Install Blueprints
    install_blueprints(app)
    print("BLUEPRINTS INSTALLED")

    # Start Flask Server
    app.run()


if __name__ == "__main__":
    # threading.Thread(target=start_flask_app, daemon=True).start()
    start_flask_app()
