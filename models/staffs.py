from init import db

class Staff(db.Model):
  __tablename__ = "staffs"
  id = db.Column(db.Integer, primary_key = True)
  name =  db.Column(db.String(100), nullable = False)
  role = db.Column(db.String(255))
  email = db.Column(db.String(255), unique = True)

  project_personnel = db.relationship("ProjectPersonnel", back_populates="staff")