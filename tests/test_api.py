import pytest
import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), os.path.pardir)))
from app import create_app
from app.student_models import db

@pytest.fixture
def client():
    app = create_app()
    app.config["TESTING"] = True
    with app.test_client() as client:
        with app.app_context():
            db.create_all()
        yield client

def test_add_student(client):
    response = client.post("/api/add_student", json={"name" : "Edwin", "age" : 20})
    assert response.status_code == 201
    assert response.json["name"] == "Edwin"