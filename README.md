# Project Cost Tracking API Server

## About the project
This project is for setting up and recording project costs during project delivery phase. Based on that, Project Manager can keep track of costs at any time during project delivery. 

The database contains 5 tables:
- projects: main information of projects
- staffs: information of staffs in the company
- project_personnel: information of project staffs
- suppliers: information of suppliers
- project_costs: information of the costs incurred throughout the projects

Features:
- Get all data in each table
- Get a specific data in each table by data id
- Filter data by specific criteria:
  - projects table: Filter projects by specific "location"
  - staffs table: Filter staffs by specific "role"
  - project_personnel table: Filter personnel by "project_id"
  - suppliers table: Filter suppliers by "name"
  - project_costs: Filter costs by "date"
- Update data in tables 
- Add new data to tables
- Delete data in tables

### How to use

First, click https://insomnia.rest/ to download and get instructions on using Insomnia 

Accessing the Web services using link: https://project-cost-tracking-api.onrender.com/
You will receive a Welcome message. 

Now follow these below routes to access and manipulate data in database tables:

- View all data in table: https://project-cost-tracking-api.onrender.com/"table name"
- View individual project data by id: https://project-cost-tracking-api.onrender.com/"table name/"table id"
- Filter data by a specific criteria: https://project-cost-tracking-api.onrender.com/"table name"?"filter column name"="criteria"

For example, filtering projects by "location" is "Sydney" in projects table using this route:
https://project-cost-tracking-api.onrender.com/projects?location=Sydney
- Add new data using Insomnia with POST request on route: https://project-cost-tracking-api.onrender.com/"table name"
- Update a specific data in table using Insomnia with PUT/PATCH request on route: https://project-cost-tracking-api.onrender.com/"table name"/"data id" 

"data id" is id of each data in table
- Add new data using Insomnia with POST request on route: https://project-cost-tracking-api.onrender.com/"table name"/"data id"
"data id" is id of each data in table


**Note**: 
- Please make sure date data always in format: "YYYY-MM-DD"
- Please ensure that you follow below data constraints in each table to avoid errors


| Table name | Data & Constraints| 
|:---------|:--------:|
| projects   | "name", "location", "client" : text, name must be unique and not be null  | 
|             | "start_date","estimate_complete_date" : Date   | 
|             | "contract_value", "budget" : number, must not be null, budget must be lower than contract_value  | 
|  | "status" : must be "Active" or "Closed"  | 
| staffs | "name", "role": text, name must not be null | 
|         | "email": email type, must be unique and not null  | 
| project_personnel | "project_role": text| 
| suppliers | "abn", "name", "sector", "address": text, name must not be null | 
|  | "email": email type, must be unique | 
| project_costs | "date": date type, must not be null | 
|  | "invoice_no", "description": text, description must not be null  | 
|  | "value": number, must not be null  | 

  - All numbers must be positive
  - All text must have more than 2 characters
  - All "id" is default generated number.
  - All date must be in format: "YYYY-MM-DD"
  - All email must be in email format "abc@def.gkh


## Future Upgrade

- Develop User Interface to perform data manipulation (POST, PUT, PATCH requests)
- Add database tables and relations, such as Client table (storing client details), Cost Code table (for project budget allocation).


