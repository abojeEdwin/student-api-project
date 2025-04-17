import logging
from flask import request, jsonify
from .student_models import db, Student

logger = logging.getLogger(__name__)

def init_routes(app):
    @app.route("/")
    def home():
        return "hello world"

    @app.route("/api/v1/healthcheck", methods=["GET"])
    def health_check():
        return jsonify({"status": "ok"}),200

    @app.route("/api/v1/students", methods=["POST"])
    def add_students():
        data = request.get_json()
        student = Student(name=data["name"], age=data["age"])
        db.session.add(student)
        db.session.commit()
        logger.info(f"Added student {student.name} added with ID {student.id}")
        return jsonify({"student" : student.to_dict()}), 201

    @app.route("/api/v1/students", methods=["GET"])
    def get_students():
        students = Student.query.all()
        return jsonify({"student" : [student.to_dict() for student in students]}), 200
