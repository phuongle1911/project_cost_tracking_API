from flask import Flask
from init import db
import os
from dotenv import load_dotenv

from controllers.cli_controller import db_commands
from controllers.project_controller import project_bp
from controllers.staff_controller import staff_bp
from controllers.project_personnel_controller import project_personnel_bp
from controllers.supplier_controller import supplier_bp
from controllers.project_cost_controller import project_cost_bp
from controllers.home_controller import homepage_bp
from utils.error_handlers import register_error_handlers

load_dotenv()

def create_app():
  app = Flask(__name__)
  app.config["SQLALCHEMY_DATABASE_URI"] = os.environ.get("DATABASE_URI")
  db.init_app(app)
  app.json.sort_keys = False

  app.register_blueprint(db_commands)
  app.register_blueprint(project_bp)
  app.register_blueprint(staff_bp)
  app.register_blueprint(project_personnel_bp)
  app.register_blueprint(supplier_bp)
  app.register_blueprint(project_cost_bp)
  app.register_blueprint(homepage_bp)
  register_error_handlers(app)
  
  return app

