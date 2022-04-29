from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

db = SQLAlchemy()
migrate = Migrate()
# connection_string = 'postgresql+psycopg2://postgres:postgres@localhost:5432/planets_development'

def create_app(test_config=None):
    app = Flask(__name__)

    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql+psycopg2://postgres:postgres@localhost:5432/planets_development'
    
    db.init_app(app)
    migrate.init_app(app, db)

    from app.routes import planet_routes
    app.register_blueprint(planet_routes.planets_bp)


    return app