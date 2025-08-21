from flask import Blueprint, jsonify, request
from init import db

from models.costs import Cost
from schemas.schemas import cost_schema, costs_schema

project_cost_bp = Blueprint("project_cost", __name__, url_prefix="/project_costs")

#Routes
# GET /project_costs/
@project_cost_bp.route("/")
def get_project_costs():
  date = request.args.get("date")
  if date:
    stmt = db.select(Cost).where(Cost.date==date)
  else:
    stmt = db.select(Cost).order_by(Cost.id)

  project_costs_list = db.session.scalars(stmt)
  data = costs_schema.dump(project_costs_list)

  if data:
    return jsonify(data)
  else:
    return {"message":"No project cost records found"}, 404
  
# GET /id
@project_cost_bp.route("/<int:cost_id>")
def get_a_project_cost(cost_id):
  stmt = db.select(Cost).where(Cost.id == cost_id)
  cost = db.session.scalar(stmt)

  if cost:
    data = cost_schema.dump(cost)
    return jsonify(data)
  else:
    return {"message":f"Cost with id {cost_id} does not exist"}, 404
  
# POST
@project_cost_bp.route("/", methods=["POST"])
def create_a_project_cost():
  # try:
  body_data = request.get_json()
  new_project_cost = cost_schema.load(
    body_data,
    session = db.session
  )
  db.session.add(new_project_cost)
  db.session.commit()
  return cost_schema.dump(new_project_cost), 201

    
# DELETE
@project_cost_bp.route("/<int:cost_id>", methods=["DELETE"])
def delete_project_cost(cost_id):
  stmt = db.select(Cost).where(Cost.id == cost_id)
  cost = db.session.scalar(stmt)

  if cost:
    db.session.delete(cost)
    db.session.commit()
    return {"message":f"Cost with id {cost_id} has been removed successfully!"}
  else:
    return {"message":f"Cost with id {cost_id} does not exist"}, 404
  

# UPDATE
@project_cost_bp.route("/<int:cost_id>", methods=["PUT","PATCH"])
def update_project_cost(cost_id):
  stmt = db.select(Cost).where(Cost.id == cost_id)
  cost = db.session.scalar(stmt)

  if not cost:
    return {"message":f"Cost with id {cost_id} does not exist"}, 404
  
  body_data = request.get_json()

  column = ["project_id","supplier_id","date","invoice_no","description","value"]
  for col in column:
    if col not in body_data.keys():
      body_data[col]=getattr(cost,col)
    else:
      pass

  updated_project_cost = cost_schema.load(
          body_data,
          instance = cost,
          session = db.session,
          partial = True
      )

  db.session.commit()
  return jsonify(cost_schema.dump(updated_project_cost)), 200
  
