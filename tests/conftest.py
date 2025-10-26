import pytest
from init import db
from flask import Flask

from controllers.cli_controller import db_commands
from controllers.project_controller import project_bp
from controllers.staff_controller import staff_bp
from controllers.project_personnel_controller import project_personnel_bp
from controllers.supplier_controller import supplier_bp
from controllers.project_cost_controller import project_cost_bp
from controllers.home_controller import homepage_bp
from utils.error_handlers import register_error_handlers

@pytest.fixture
def client():
  app = Flask(__name__)
  app.config["TESTING"] = True
  app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///:memory:"
  

  app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
  db.init_app(app)

  app.register_blueprint(db_commands)
  app.register_blueprint(project_bp)
  app.register_blueprint(staff_bp)
  app.register_blueprint(project_personnel_bp)
  app.register_blueprint(supplier_bp)
  app.register_blueprint(project_cost_bp)
  app.register_blueprint(homepage_bp)
  register_error_handlers(app)

  with app.app_context():
    db.create_all()
    yield app.test_client()
    db.session.remove()
    db.drop_all()





