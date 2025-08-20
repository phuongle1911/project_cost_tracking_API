from flask import Blueprint, jsonify, request
from init import db

from models.staffs import Staff
from schemas.schemas import staff_schema, staffs_schema

staff_bp = Blueprint("staff", __name__, url_prefix="/staffs")

#Routes
# GET /staffs/
@staff_bp.route("/")
def get_staffs():
  role = request.args.get("role")
  if role:
    stmt = db.select(Staff).where(Staff.role==role)
  else:
    stmt = db.select(Staff).order_by(Staff.id)

  staffs_list = db.session.scalars(stmt)
  data = staffs_schema.dump(staffs_list)

  if data:
    return jsonify(data)
  else:
    return {"message":"No staff records found"}, 404
  
# GET /id
@staff_bp.route("/<int:staff_id>")
def get_a_staff(staff_id):
  stmt = db.select(Staff).where(Staff.id == staff_id)
  staff = db.session.scalar(stmt)

  if staff:
    data = staff_schema.dump(staff)
    return jsonify(data)
  else:
    return {"message":f"Staff with id {staff_id} does not exist"}, 404
  
# POST
@staff_bp.route("/", methods=["POST"])
def create_a_staff():
  # try:
  body_data = request.get_json()
  new_staff = staff_schema.load(
    body_data,
    session = db.session
  )
  db.session.add(new_staff)
  db.session.commit()
  return staff_schema.dump(new_staff), 201

    
# DELETE
@staff_bp.route("/<int:staff_id>", methods=["DELETE"])
def delete_staff(staff_id):
  stmt = db.select(Staff).where(Staff.id == staff_id)
  staff = db.session.scalar(stmt)

  if staff:
    db.session.delete(staff)
    db.session.commit()
    return {"message":f"Staff {staff.name} has been removed successfully!"}
  else:
    return {"message":f"Staff with id {staff_id} does not exist"}, 404
  

# UPDATE
@staff_bp.route("/<int:staff_id>", methods=["PUT","PATCH"])
def update_staff(staff_id):
  stmt = db.select(Staff).where(Staff.id == staff_id)
  staff = db.session.scalar(stmt)

  if not staff:
    return {"message":f"Staff with id {staff_id} does not exist"}, 404
  
  body_data = request.get_json()
  # body_data.name = staff.name if not body_data.name else body_data.name
  column = ["name","role","email"]
  for col in column:
    if col not in body_data.keys():
      body_data[col]=getattr(staff,col)
    else:
      pass

  updated_staff = staff_schema.load(
          body_data,
          instance = staff,
          session = db.session,
          partial = True
      )

  db.session.commit()
  return jsonify(staff_schema.dump(updated_staff)), 200