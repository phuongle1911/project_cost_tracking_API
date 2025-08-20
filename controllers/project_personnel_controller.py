from flask import Blueprint, jsonify, request
from init import db

from models.project_personnel import ProjectPersonnel
from models.staffs import Staff
from models.projects import Project
from schemas.schemas import project_personnel_schema, project_personnels_schema

project_personnel_bp = Blueprint("project_personnel", __name__, url_prefix="/project_personnel")

#Routes
# GET /project_personnel/
@project_personnel_bp.route("/")
def get_project_personnel():
  project_id = request.args.get("project_id")
  if project_id:
    stmt = db.select(ProjectPersonnel).where(ProjectPersonnel.project_id==project_id)
  else:
    stmt = db.select(ProjectPersonnel).order_by(ProjectPersonnel.project_id)

  project_personnel_list = db.session.scalars(stmt)
  data = project_personnels_schema.dump(project_personnel_list)

  if data:
    return jsonify(data)
  else:
    return {"message":"No project personnel records found"}, 404
  
# GET /project_id/staff_id
@project_personnel_bp.route("/<int:project_id>/<int:staff_id>")
def get_a_project_personnel(project_id, staff_id):
  stmt = db.select(ProjectPersonnel).where((ProjectPersonnel.project_id == project_id),(ProjectPersonnel.staff_id==staff_id))
  project_personnel = db.session.scalar(stmt)

  if project_personnel:
    data = project_personnel_schema.dump(project_personnel)
    return jsonify(data)
  else:
    return {"message":f"No record found in project id {project_id} for personnel with staff id {staff_id}."}, 404
  
# POST
@project_personnel_bp.route("/", methods=["POST"])
def create_a_project_personnel():
  # try:
  body_data = request.get_json()
  new_project_personnel = project_personnel_schema.load(
    body_data,
    session = db.session
  )
  db.session.add(new_project_personnel)
  db.session.commit()
  return project_personnel_schema.dump(new_project_personnel), 201

    
# DELETE
@project_personnel_bp.route("/<int:project_id>/<int:staff_id>", methods=["DELETE"])
def delete_project_personnel(project_id, staff_id):
  stmt = db.select(ProjectPersonnel).where(ProjectPersonnel.project_id == project_id, ProjectPersonnel.staff_id==staff_id)
  project_personnel = db.session.scalar(stmt)

  if project_personnel:
    db.session.delete(project_personnel)
    db.session.commit()
    return {"message":f"Staff with id {project_personnel.staff_id} has been removed successfully from project id {project_personnel.project_id}!"}
  else:
    return {"message":f"No record found in project id {project_id} for personnel with staff id {staff_id}"}, 404
  

# UPDATE
@project_personnel_bp.route("/<int:project_id>/<int:staff_id>", methods=["PUT","PATCH"])
def update_project_personnel(project_id, staff_id):
  stmt = db.select(ProjectPersonnel).where(ProjectPersonnel.project_id == project_id,ProjectPersonnel.staff_id==staff_id)
  project_personnel = db.session.scalar(stmt)

  # staff_stmt = db.select(Staff).where(Staff.id == staff_id)
  # staff = db.session.scalar(staff_stmt)

  # if not staff:
  #   return {"message":f"Staff id {staff_id} does not exist"}
  if not project_personnel:
    return {"message":f"No record found for project id {project_id} and personnel with staff id {staff_id}"}, 404
  
  body_data = request.get_json()
  # body_data.name = project_personnel.name if not body_data.name else body_data.name
  column = ["project_id","staff_id","project_role"]
  for col in column:
    if col not in body_data.keys():
      body_data[col]=getattr(project_personnel,col)
    else:
      pass

  updated_project_personnel = project_personnel_schema.load(
          body_data,
          instance = project_personnel,
          session = db.session,
          partial = True
      )

  db.session.commit()
  return jsonify(project_personnel_schema.dump(updated_project_personnel)), 200
  
