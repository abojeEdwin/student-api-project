import logging
from flask import Flask
from .config import Config
from .student_models import db

logging.basicConfig(level = logging.INFO)
logger = logging.getLogger(__name__)

def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)
    db.init_app(app)
    with app.app_context():
        db.create_all()
        logger.info(f"Database tables created")
    from .routes import init_routes
    init_routes(app)
    return app