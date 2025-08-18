from flask import Flask
from init import db
import os
from dotenv import load_dotenv

from controllers.cli_controller import db_commands
from controllers.project_controller import project_bp
from utils.error_handlers import register_error_handlers

load_dotenv()

def create_app():
  app = Flask(__name__)
  app.config["SQLALCHEMY_DATABASE_URI"] = os.environ.get("DATABASE_URI")
  db.init_app(app)

  app.register_blueprint(db_commands)
  app.register_blueprint(project_bp)
  register_error_handlers(app)
  
  return app

