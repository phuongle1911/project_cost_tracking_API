from flask import Blueprint, jsonify, request
from init import db
from marshmallow import ValidationError
from sqlalchemy.exc import IntegrityError
from psycopg2 import errorcodes

from models.projects import Project
from schemas.schemas import project_schema, projects_schema

project_bp = Blueprint("project", __name__, url_prefix="/projects")

#Routes
# GET /projects/
@project_bp.route("/")
def get_projects():
  stmt = db.select(Project)
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
  # except IntegrityError as err:
  #   if err.orig.pgcode == errorcodes.NOT_NULL_VIOLATION:
  #     return {"message":f"Required field {err.orig.diag.column_name} cannot be null"}, 400
  #   if err.orig.pgcode == errorcodes.UNIQUE_VIOLATION:
  #     return (err.orig.diag.message_primary), 400
  #   else:
  #     return {"message": f"Unexpected error occured. Details: {err.messages}"}, 400
  # except ValidationError as err:
  #   return err.messages, 400
    
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
  
  # try:
  body_data = request.get_json()
  project.name = body_data.get("name") or project.name
  project.client = body_data.get("client") or project.client
  project.location = body_data.get("location") or project.location
  project.start_date = body_data.get("start_date") or project.start_date
  project.estimate_completion_date = body_data.get("estimate_completion_date") or project.estimate_completion_date
  project.status = body_data.get("status") or project.status
  project.contract_value = body_data.get("contract_value") or project.contract_value
  project.budget = body_data.get("budget") or project.budget

  db.session.commit()
  return jsonify(project_schema.dump(project)), 200
  
  # except IntegrityError as err:
  #   if err.orig.pgcode == errorcodes.NOT_NULL_VIOLATION:
  #     return {"message":f"Required field {err.orig.diag.column_name} cannot be null"}, 400
  #   if err.orig.pgcode == errorcodes.UNIQUE_VIOLATION:
  #     return {"message":f"{err.orig.diag.column_name} existed in the data set. This needs to be unique."}, 400
  #   else:
  #     return {"message": f"Unexpected error occured. Details: {err.messages}"}, 400
    
  # except ValidationError as err:
  #   return {"message": "data constraint failed. Possibly a duplicate or null value"}, 400

