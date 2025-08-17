from init import db
from datetime import date

class Project(db.Model):
  __tablename__ = "projects"
  id = db.Column(db.Integer, primary_key = True)
  name =  db.Column(db.String(255), nullable = False, unique = True)
  client = db.Column(db.String(100))
  location = db.Column(db.String(255))
  start_date = db.Column(db.Date)
  estimate_completion_date = db.Column(db.Date)
  status = db.Column(db.String(100))
  contract_value = db.Column(db.Integer, nullable = False)
  budget = db.Column(db.Integer, nullable = False)

  project_personnel = db.relationship("ProjectPersonnel", back_populates="project")
  project_costs = db.relationship("Cost", back_populates="project")



