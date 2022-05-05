import pytest
from flask.signals import request_finished
from app import db
from app import create_app
from app.models.planet import Planet

@pytest.fixture
def app():
    app = create_app({"TESTING": True})

    @request_finished.connect_via(app)
    def expire_session(sender, response, **extra):
        db.session.remove()
    
    with app.app_context():
        db.create_all()
        yield app
    
    with app.app_context():
        db.drop_all()

@pytest.fixture
def client(app):
    return app.test_client()

@pytest.fixture
def two_planets(app):
    Earth = Planet(id=1, name="Earth", description="home", life="True", moons="luna")
    Mars = Planet(id=2, name="Mars", description="1st Colony", life="True", moons="None")

    db.session.add(Earth)
    db.session.add(Mars)
    db.session.commit()