from init import db

class Cost(db.Model):
  __tablename__ = "project_costs"
#   __table_args__ = (
#   db.PrimaryKeyConstraint("supplier_ABN", "invoice_no"),
#   db.UniqueConstraint("supplier_ABN", "invoice_no", name = "unique_supplier_invoice"),
# )
  id = db.Column(db.Integer, primary_key = True)
  project_id =  db.Column(db.Integer, db.ForeignKey("projects.id"), nullable = False)
  supplier_id = db.Column(db.Integer, db.ForeignKey("suppliers.id"))
  date = db.Column(db.Date, nullable = False)
  invoice_no = db.Column(db.String(100))
  description = db.Column(db.String(255),nullable = False)
  value = db.Column(db.Integer, nullable = False)

  project = db.relationship("Project", back_populates="project_costs")
  supplier = db.relationship("Supplier", back_populates="project_costs")