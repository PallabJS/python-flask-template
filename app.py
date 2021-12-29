import config
import os
from flask import Flask
from flask_cors import CORS

from app_utils import initialize_app


# Initialize flask app
app = Flask(__name__)
CORS(app)


@app.route("/", methods=["GET"])
def base_route():
    return {"status": "ok"}


if __name__ == "__main__":

    # App initializer
    initialize_app(app)

    if config.env == "production":
        app.run(host="0.0.0.0", port=os.getenv("PORT"))
    else:
        app.run(port=8000, debug=True, threaded=True,
                use_reloader=True, use_debugger=True)
