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
        db.session.remove()
        db.drop_all()
def set_up():
    db.drop_all()

def tear_down():
    db.drop_all()

def test_add_student(client):
    response = client.post("/api/v1/students", json={"name" : "Edwin", "age" : 20})
    assert response.status_code == 201
    assert response.json["student"]["name"] == "Edwin"


def test_get_students(client):
    response1 = client.post("/api/v1/students", json={"name": "Edwin", "age": 20})
    response = client.get("/api/v1/students")
    assert response.status_code == 200
    assert len(response.json["student"]) == 1