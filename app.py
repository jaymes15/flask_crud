from config import Config
from flask import Flask
from flask_cors import CORS
from flask_smorest import Api
from flask_migrate import Migrate

from db import db
from integrations.configure_jwt import configure_jwt
from routes.register_routes import register_routes
from dotenv import load_dotenv


load_dotenv()


def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)
    CORS(app)
    db.init_app(app)
    Migrate(app, db)
    api = Api(app)
    configure_jwt(app)
    register_routes(api=api)

    return app
