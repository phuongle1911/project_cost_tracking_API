from flask import Blueprint, jsonify, request
from init import db

from models.projects import Project
from schemas.schemas import project_schema, projects_schema

project_bp = Blueprint("project", __name__, url_prefix="/projects")

#Routes
# GET /projects/
@project_bp.route("/")
def get_projects():
  location = request.args.get("location")
  if location:
    stmt = db.select(Project).where(Project.location==location)
  else:
    stmt = db.select(Project).order_by(Project.id)

  projects_list = db.session.scalars(stmt)
  data = projects_schema.dump(projects_list)

  if data:
    return jsonify(data)
  else:
    return {"message":"No project records found"}, 404
  
# GET /id
@project_bp.route("/<int:project_id>")
def get_a_project(project_id):
  stmt = db.select(Project).where(Project.id == project_id)
  project = db.session.scalar(stmt)

  if project:
    data = project_schema.dump(project)
    return jsonify(data)
  else:
    return {"message":f"Project with id {project_id} does not exist"}, 404
  
# POST
@project_bp.route("/", methods=["POST"])
def create_a_project():
  # try:
  body_data = request.get_json()
  new_project = project_schema.load(
    body_data,
    session = db.session
  )
  db.session.add(new_project)
  db.session.commit()
  return project_schema.dump(new_project), 201

    
# DELETE
@project_bp.route("/<int:project_id>", methods=["DELETE"])
def delete_project(project_id):
  stmt = db.select(Project).where(Project.id == project_id)
  project = db.session.scalar(stmt)

  if project:
    db.session.delete(project)
    db.session.commit()
    return {"message":f"Project {project.name} has been removed successfully!"}
  else:
    return {"message":f"Project with id {project_id} does not exist"}, 404
  

# UPDATE
@project_bp.route("/<int:project_id>", methods=["PUT","PATCH"])
def update_project(project_id):
  stmt = db.select(Project).where(Project.id == project_id)
  project = db.session.scalar(stmt)

  if not project:
    return {"message":f"Project with id {project_id} does not exist"}, 404
  
  body_data = request.get_json()
  # body_data.name = project.name if not body_data.name else body_data.name
  column = ["name","client","location","start_date","estimate_completion_date","status","contract_value","budget"]
  for col in column:
    if col not in body_data.keys():
      body_data[col]=getattr(project,col)
    else:
      pass

  updated_project = project_schema.load(
          body_data,
          instance = project,
          session = db.session,
          partial = True
      )

  db.session.commit()
  return jsonify(project_schema.dump(updated_project)), 200
  
