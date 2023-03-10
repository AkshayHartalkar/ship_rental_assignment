"""
    Generic template for creating test client
"""

import pytest
from flask_app import create_app

@pytest.fixture
def app():

    app = create_app({
        'TESTING': True,
    })

    yield app

@pytest.fixture
def client(app):
    return app.test_client()

@pytest.fixture
def runner(app):
    return app.test_cli_runner()