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
      abn= "04 526 384 700",
      name="Microsoft",
      sector="software",
      address="Sydney",
      email="sales@microsoft.com.au"
    ),
    Supplier(
      abn="65 000 087 936",
      name="Jaycar",
      sector="hardware",
      address="Notting Hill, VIC",
      email="sales@jaycar.com.au"
    ),
    Supplier(
      abn="63 605 345 891",
      name="Amazon Web Services",
      sector="cloud computing",
      address="Sydney",
      email="sales@amazon.com.au"
    ),
    Supplier(
      abn="37 093 114 286",
      name="JB Hifi",
      sector="hardware",
      address="Melbourne",
      email="sales@jbhifi.com.au"
    ),
  ]

  db.session.add_all(suppliers)

  project_personnel=[
    ProjectPersonnel(
      staff=staffs[3],
      project=projects[0],
      project_role="Project Manager"
    ),
    ProjectPersonnel(
      staff=staffs[0],
      project=projects[0],
      project_role="Tester"
    ),
    ProjectPersonnel(
      staff=staffs[2],
      project=projects[0],
      project_role="Developer"
    ),
    ProjectPersonnel(
      staff=staffs[3],
      project=projects[1],
      project_role="Project Manager"
    ),
     ProjectPersonnel(
      staff=staffs[1],
      project=projects[1],
      project_role="Tester"
    ),
    ProjectPersonnel(
      staff=staffs[0],
      project=projects[1],
      project_role="Developer"
    ),
     ProjectPersonnel(
      staff=staffs[3],
      project=projects[2],
      project_role="Project Manager"
    ),
    ProjectPersonnel(
      staff=staffs[2],
      project=projects[2],
      project_role="Developer"
    ),
    ProjectPersonnel(
      staff=staffs[0],
      project=projects[2],
      project_role="Tester"
    ),
    ProjectPersonnel(
      staff=staffs[1],
      project=projects[2],
      project_role="Support Engineer"
    ),
    ProjectPersonnel(
      staff=staffs[4],
      project=projects[2],
      project_role="Project Director"
    )
  ]

  db.session.add_all(project_personnel)

  project_costs = [
    Cost(
      project=projects[0],
      supplier=suppliers[1],
      date="2024-06-30",
      invoice_no="INV2067",
      description="Wifi router",
      value=2299
    ),
    Cost(
      project=projects[0],
      supplier=suppliers[2],
      date="2024-12-20",
      invoice_no="INV1746",
      description="AWS subscription",
      value=1230
    ),
    Cost(
      project=projects[0],
      date="2024-10-30",
      description="labour 20/6/24 to 30/10/24",
      value=15550
    ),
    Cost(
      project=projects[0],
      date="2025-01-31",
      description="labour 31/10/24 to 31/01/25",
      value=10400
    ),
    Cost(
      project=projects[1],
      supplier=suppliers[0],
      date="2025-04-22",
      invoice_no="INV3155",
      description="Microsoft subscription",
      value=2453
    ),
    Cost(
      project=projects[1],
      date="2025-06-30",
      description="labour 1/2/25 to 30/6/25",
      value=15300
    ),
    Cost(
      project=projects[2],
      supplier=suppliers[3],
      date="2025-03-19",
      invoice_no="INV1722",
      description="Hard drive",
      value=1250
    ),
    Cost(
      project=projects[2],
      supplier=suppliers[2],
      date="2025-02-27",
      invoice_no="INV6800",
      description="AWS plugin",
      value=600
    ),
    Cost(
      project=projects[2],
      date="2025-07-30",
      description="labour from 1/2/25 to 30/7/25",
      value=13400
    ),
    Cost(
      project=projects[2],
      supplier=suppliers[3],
      date="2024-06-30",
      invoice_no="INV3788",
      description="Macbook laptop",
      value=3299
    ),
  ]

  db.session.add_all(project_costs)

  db.session.commit()
  print("Table seeded!")