import pytest
 
from flask import Flask
from flaskr import create_app

@pytest.fixture
def app():     
    app = create_app()
    app.config['TESTING'] = True
    yield app
     
@pytest.fixture
def client(app):
    return app.test_client()
    
