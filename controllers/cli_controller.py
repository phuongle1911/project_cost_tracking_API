from flask import Blueprint
from init import db

from models.projects import Project
from models.project_personnel import ProjectPersonnel
from models.staffs import Staff
from models.costs import Cost
from models.suppliers import Supplier

db_commands = Blueprint("db",__name__)

@db_commands.cli.command("create")
def create_tables():
  db.create_all()
  print("Tables created!")

@db_commands.cli.command("drop")
def drop_tables():
  db.drop_all()
  print("Tables dropped!")

@db_commands.cli.command("seed")
def seed_tables():
  projects = [
    Project(
      name="Allianz website development",
      client="Allianz",
      location="Melbourne",
      start_date="2024-06-24",
      estimate_completion_date="2025-02-20",
      status="Closed",
      contract_value=30000,
      budget=25000
    ),
    Project(
      name="ANZ commercial application development",
      client="ANZ",
      location="Sydney",
      start_date="2025-01-10",
      estimate_completion_date="2025-06-15",
      status="Active",
      contract_value=60000,
      budget=40000
    ),
    Project(
      name="Sport application development",
      client="Snap Fitness",
      location="Melbourne",
      start_date="2025-04-15",
      estimate_completion_date="2025-10-30",
      status="Active",
      contract_value=100000,
      budget=80000
    )
  ]

  db.session.add_all(projects)
  
  staffs = [
    Staff(
      name = "Alice Spring",
      role = "Junior Developer",
      email = "alice.s@pldigital.com"
    ),
    Staff(
      name = "Jake Moffa",
      role = "Junior Developer",
      email = "jake.m@pldigital.com"
    ),
    Staff(
      name = "Luke Nolder",
      role = "Software Developer",
      email = "luke.n@pldigital.com"
    ),
    Staff(
      name = "Shaun Brand",
      role = "Senior Developer",
      email = "shaun.b@pldigital.com"
    ),
    Staff(
      name = "Phuong Le",
      role = "Manager",
      email = "phuong.l@pldigital.com"
    )
  ]

  db.session.add_all(staffs)

  suppliers = [
    Supplier(
      name="Microsoft",
      sector="software",
      address="Sydney CBD",
      email="sales@microsoft.com.au"
    ),
    Supplier(
      name="Microsoft",
      sector="software",
      address="Sydney CBD",
      email="sales@microsoft.com.au"
    ),
    Supplier(
      name="Microsoft",
      sector="software",
      address="Sydney CBD",
      email="sales@microsoft.com.au"
    ),
    Supplier(
      name="Microsoft",
      sector="software",
      address="Sydney CBD",
      email="sales@microsoft.com.au"
    ),
  ]