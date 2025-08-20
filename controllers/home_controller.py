from flask import Blueprint
from init import db

homepage_bp = Blueprint("homepage",__name__)

@homepage_bp.route("/")
def get_homepage():
  return "<h1>Welcome to Project Cost Tracking website<h1>!"