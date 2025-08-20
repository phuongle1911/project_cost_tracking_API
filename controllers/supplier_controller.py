from flask import Blueprint, jsonify, request
from init import db

from models.suppliers import Supplier
from schemas.schemas import supplier_schema, suppliers_schema

supplier_bp = Blueprint("supplier", __name__, url_prefix="/suppliers")

#Routes
# GET /suppliers/
@supplier_bp.route("/")
def get_suppliers():
  name = request.args.get("name")
  if name:
    stmt = db.select(Supplier).where(Supplier.name==name)
  else:
    stmt = db.select(Supplier).order_by(Supplier.id)

  suppliers_list = db.session.scalars(stmt)
  data = suppliers_schema.dump(suppliers_list)

  if data:
    return jsonify(data)
  else:
    return {"message":"No supplier records found"}, 404
  
# GET /id
@supplier_bp.route("/<int:supplier_id>")
def get_a_supplier(supplier_id):
  stmt = db.select(Supplier).where(Supplier.id == supplier_id)
  supplier = db.session.scalar(stmt)

  if supplier:
    data = supplier_schema.dump(supplier)
    return jsonify(data)
  else:
    return {"message":f"Supplier with id {supplier_id} does not exist"}, 404
  
# POST
@supplier_bp.route("/", methods=["POST"])
def create_a_supplier():
  # try:
  body_data = request.get_json()
  new_supplier = supplier_schema.load(
    body_data,
    session = db.session
  )
  db.session.add(new_supplier)
  db.session.commit()
  return supplier_schema.dump(new_supplier), 201

    
# DELETE
@supplier_bp.route("/<int:supplier_id>", methods=["DELETE"])
def delete_supplier(supplier_id):
  stmt = db.select(Supplier).where(Supplier.id == supplier_id)
  supplier = db.session.scalar(stmt)

  if supplier:
    db.session.delete(supplier)
    db.session.commit()
    return {"message":f"Supplier {supplier.name} has been removed successfully!"}
  else:
    return {"message":f"Supplier with id {supplier_id} does not exist"}, 404
  

# UPDATE
@supplier_bp.route("/<int:supplier_id>", methods=["PUT","PATCH"])
def update_supplier(supplier_id):
  stmt = db.select(Supplier).where(Supplier.id == supplier_id)
  supplier = db.session.scalar(stmt)

  if not supplier:
    return {"message":f"Supplier with id {supplier_id} does not exist"}, 404
  
  body_data = request.get_json()
  column = ["abn","name","sector","address","email"]
  for col in column:
    if col not in body_data.keys():
      body_data[col]=getattr(supplier,col)
    else:
      pass

  updated_supplier = supplier_schema.load(
          body_data,
          instance = supplier,
          session = db.session,
          partial = True
      )

  db.session.commit()
  return jsonify(supplier_schema.dump(updated_supplier)), 200
  
