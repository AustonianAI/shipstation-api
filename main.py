from flask import Flask, jsonify
from flask_smorest import Api
import os


# Resources
from resources.shipstation import blp as ShipStationBlueprint

# API Configuration
app = Flask(__name__)
app.config["API_TITLE"] = "HatcheryBrain Manager"
app.config["API_VERSION"] = "v1"
app.config["OPENAPI_VERSION"] = "3.0.2"

api = Api(app)

# Registering Blueprints
api.register_blueprint(ShipStationBlueprint)


api.init_app(app)


@app.route('/')
def index():
    return jsonify(
        {"Choo Choo": "Welcome to your Flask app 🚅"}
    )


if __name__ == '__main__':
    app.run(debug=True, port=os.getenv("PORT", default=5000))
