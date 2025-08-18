from init import db

class Supplier(db.Model):
  __tablename__ = "suppliers"
  id = db.Column(db.Integer, primary_key = True)
  abn = db.Column(db.String(50), unique = True)
  name =  db.Column(db.String(100), nullable = False)
  sector = db.Column(db.String(255))
  address = db.Column(db.String(255))
  email = db.Column(db.String(255), unique = True)

  project_costs = db.relationship("Cost", back_populates="supplier")
