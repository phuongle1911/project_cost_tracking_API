from init import db

class ProjectPersonnel(db.Model):
  __tablename__ = "project_personnel"
  __table_args__ = (
  db.PrimaryKeyConstraint("project_id", "staff_id"),
  db.UniqueConstraint("project_id", "staff_id", name = "unique_project_staff"),
)

  project_id = db.Column(db.Integer, db.ForeignKey("projects.id"), primary_key = True)
  staff_id = db.Column(db.Integer, db.ForeignKey("staffs.id"), primary_key = True)
  project_role = db.Column(db.String(255))

  project = db.relationship("Project", back_populates="project_personnel")
  staff = db.relationship("Staff", back_populates="project_personnel")
