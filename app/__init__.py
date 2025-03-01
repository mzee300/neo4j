from flask import Flask
from neomodel import config
from config import config as app_config

def create_app(config_name="default"):
    app = Flask(__name__)

    app.config.from_object(app_config[config_name])

    config.DATABASE_URL = (
        f"bolt://{app.config['NEO4J_USER']}:{app.config['NEO4J_PASSWORD']}"
        f"@{app.config['NEO4J_HOST']}:{app.config['NEO4J_PORT']}"
    )

    from app.routes import register_blueprints
    register_blueprints(app)

    return app
