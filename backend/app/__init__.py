from flask import Flask, jsonify
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()


def create_app(env):
    from app.config import config_names
    from app.youtube_money_calculator.controllers import channels

    app = Flask(__name__)
    app.config.from_object(config_names[env])
    db.init_app(app)
    app.register_blueprint(channels, url_prefix="/channels")

    @app.route("/")
    def index():
        return jsonify("Youtube Money Calculator")

    return app
