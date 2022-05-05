from dotenv import load_dotenv
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
import os

db = SQLAlchemy()
migrate = Migrate()
# connection_string = 'postgresql+psycopg2://postgres:postgres@localhost:5432/planets_development'

def create_app(test_config=None):
    app = Flask(__name__)

    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    if test_config is None:
        app.config["SQLALCHEMY_DATABASE_URI"] = os.environ.get("SQLALCHEMY_DATABASE_URI")
    else:
        app.config["TESTING"] = True
        app.config["SQLALCHEMY_DATABASE_URI"] = os.environ.get("SQLALCHEMY_DATABASE_TEST_URI")
    
    db.init_app(app)
    migrate.init_app(app, db)

    from app.routes import planet_routes
    app.register_blueprint(planet_routes.planets_bp)


    return app