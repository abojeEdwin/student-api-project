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

def set_up():
    db.drop_all()
    db.session.delete()

def tear_down():
    db.drop_all()
    db.session.delete()

def test_add_student(client):
    response = client.post("/api/v1/students", json={"name" : "Edwin", "age" : 20})
    assert response.status_code == 201
    assert response.json["student"]["name"] == "Edwin"


def test_get_students(client):
    response1 = client.post("/api/v1/students", json={"name": "Edwin", "age": 20})
    response = client.get("/api/v1/students")
    assert response.status_code == 200
    assert len(response.json["student"]) == 1

def test_get_student(client):
    response1 = client.post("/api/v1/students", json={"name": "Edwin", "age": 20})
    student_id = response1.json["student"]["id"]
    response = client.get(f"/api/v1/students/{student_id}")
    assert response.status_code == 200
    assert response.json["name"] == "Edwin"
    assert response.json["age"] == 20

def test_update_student(client):
    response1 = client.post("/api/v1/students", json={"name": "Edwin", "age": 20})
    student_id = response1.json["student"]["id"]
    response = client.put(f"/api/v1/students/{student_id}", json={"name": "Edwin", "age": 21})
    assert response.status_code == 200
    assert response.json["name"] == "Edwin"
    assert response.json["age"] == 21


def test_delete_student(client):
    response = client.post("/api/v1/students", json={"name": "Mike Tyson", "age": 20})
    student_id = response.json["student"]["id"]
    response1 = client.delete(f"/api/v1/students/{student_id}")
    assert response1.status_code == 204
