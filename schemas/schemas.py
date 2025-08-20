from marshmallow_sqlalchemy import SQLAlchemyAutoSchema, auto_field
from marshmallow import fields, validate, validates, validates_schema, ValidationError
from marshmallow.validate import OneOf, Length, Email

from models.projects import Project
from models.project_personnel import ProjectPersonnel
from models.staffs import Staff
from models.costs import Cost
from models.suppliers import Supplier

class StaffSchema(SQLAlchemyAutoSchema):
  class Meta:
    model = Staff
    load_instance = True
    include_relationships = True
    fields = ("id","name","role","email")
    ordered = True

  name = auto_field(validate=Length(min=3))
  role = auto_field(validate=Length(min=2))
  email = auto_field(validate=Email(error="Invalid Email Address"))

  project_personnel = fields.List(fields.Nested("ProjectPersonnelSchema"))

class ProjectPersonnelSchema(SQLAlchemyAutoSchema):
  class Meta:
    model = ProjectPersonnel
    load_instance = True
    include_fk = True
    include_relationships = True
    # fields = ("staff_id","project_id","project_role")
    ordered = True    

  project_role = auto_field(validate=Length(min=2))

  project = fields.Nested("ProjectSchema", only = ("name","status",))
  staff = fields.Nested("StaffSchema", only=("name",))

class ProjectSchema(SQLAlchemyAutoSchema):
  class Meta:
    model = Project
    load_instance = True
    include_relationships = True
    fields = ("id","name","client","location","start_date","estimate_completion_date","status","contract_value","budget")
    ordered = True

  # validate data
  @validates("name","client","location")
  def validate_string(self, value, data_key):
    if len(value) < 3:
      raise ValidationError("Invalid input! String is too short!")
    
  @validates_schema
  def validate_date(self,data,**kwargs):
    if data["start_date"] and data["estimate_completion_date"]:
      if data["start_date"] > data["estimate_completion_date"]:
        raise ValidationError("Invalid date! Completion date must be later than start date!")
      if data["budget"] >= data["contract_value"]:
        raise ValidationError("Invalid budget value! Budget must be lower than contract value.")
      

  @validates("contract_value","budget")
  def validate_number(self, value, data_key):
    if value <= 0:
      raise ValidationError("Invalid contract value/ budget value! Value must be greater than 0!")
    
  status = auto_field(validate=OneOf(["Active","Closed"],
                  error = "Invalid status! Only valid status are: Active, Closed"))
  
  project_personnel = fields.List(fields.Nested("ProjectPersonnelSchema", exclude=("project_id",)))
  project_costs = fields.List(fields.Nested("CostSchema", only =("date","description","value",)))

class CostSchema(SQLAlchemyAutoSchema):
  class Meta:
    model = Cost
    load_instance = True
    include_fk = True
    include_relationships = True
    # fields = ("id","supplier_id","date","invoice_no","project_id","description","value")
    ordered = True
  
  @validates("invoice_no","description")
  def validate_string(self, value, data_key):
    if len(value) < 3:
      raise ValidationError("Invalid text input! Text is too short!")
    
  @validates("value")
  def validate_number(self, value, data_key):
    if value <= 0:
      raise ValidationError("Invalid Spending value! Value must be greater than 0!")

  project = fields.Nested("ProjectSchema",only=("name",))
  supplier = fields.Nested("SupplierSchema", only=("name", "address",))

class SupplierSchema(SQLAlchemyAutoSchema):
  class Meta:
      model = Supplier
      load_instance = True
      include_relationships = True
      fields = ("id","abn","name", "sector","address","email")
      ordered = True  

  @validates("abn","name","sector","address")
  def validate_string(self, value, data_key):
    if len(value) < 3:
      raise ValidationError("Invalid text input! Text is too short!")
    
  email = auto_field(validate=Email(error="Invalid Email Address"))

  project_costs = fields.List(fields.Nested("CostSchema",exclude=("supplier_id",)))

staff_schema = StaffSchema()
staffs_schema = StaffSchema(many=True)

project_personnel_schema = ProjectPersonnelSchema()
project_personnels_schema = ProjectPersonnelSchema(many=True)

project_schema = ProjectSchema()
projects_schema = ProjectSchema(many=True)

cost_schema = CostSchema()
costs_schema = CostSchema(many=True)

supplier_schema = SupplierSchema()
suppliers_schema = SupplierSchema(many=True)