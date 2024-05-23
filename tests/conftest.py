import os
import sys

import pytest
project_directory = os.path.abspath(os.path.join(os.path.dirname(__file__), "../app"))
sys.path.append(project_directory)
from app import create_app
from database import db, init_app


@pytest.fixture
def app():
    app = create_app()
    app.config.from_object('config.TestingConfig')
    with app.app_context():
        db.create_all()
        yield app
        db.session.remove()  # looks like db.session.close() would work as well
        db.drop_all()


@pytest.fixture()
def client(app):
    return app.test_client()


@pytest.fixture()
def runner(app):
    return app.test_cli_runner()