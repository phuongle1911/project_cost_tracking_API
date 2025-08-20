- add error handler database message
- add error handler for wrong data type for date
- add more error handling for another error codes
- fix post request in project personnel, still post new data even violate unique constraint. However, this works fine with Patch request

# Project Cost Tracking API Server

## About the project
This project is for setting up and recording project costs during project delivery phase. Based on that, Project Manager can keep track of costs at any time during project delivery. 

The database contains 5 tables:
- projects: main information of projects
- staffs: information of staffs in the company
- project_personnel: information of project staffs
- suppliers: information of suppliers
- project_costs: information of the costs incurred throughout the projects

Accessing the Web services using link: https://project-cost-tracking-api.onrender.com/
You will receive a Welcome message. 

Now follow these below routes to access and maipulate datas in database tables:

- View all data in table: https://project-cost-tracking-api.onrender.com/"table name"
- View individual project data by id: https://project-cost-tracking-api.onrender.com/projects/"insert table id here"
 

## Feedbacks 

### Feedback 1
Feedback received by Aamod on below initial diagram:
- There's a one to many relationship from projects to "incurred costs", and also from the junction table "cost_allocation" to "incurred costs". Maybe avoid the junction table connection. If you do plan to keep the connection:
  
- Have a separate PK in the junction tableIt works as a FK in the "incurred costs" table.

- The concept of "Incurred costs" and "Cost Allocation" seems redundant.
responsible_staff in "incurred costs" table, is it supposed to track staff? If so, a good idea is to create a staffs table and link it (normalisation would help here).

- You have "project manager" as well. So maybe project manager can link to "staffs" table?

- Because you have project start, completion dates, you could also add a "status" attribute to the "projects" table that has (active, completed, cancelled, or something similar).
![alt text](<images/ERD ver1.png>)

**Actions**:
- Remove project_cost_summary, cost_allocation and cost_codes tables. The reasons are:
  - project_cost_summary data are calculated from project budget data and cost data, which are in projects and costs tables. Therefore, project_cost_summary table is redundant.  
  - cost allocation and cost_codes tables are not essential at this project development stage, therefore being removed. These will be considered to integrate in the next stage. 
- Data Normalisation:
  - Creating staffs table, and a conjunction table "project_personnel" connecting projects and staffs tables. 
  - Normalise costs table containing only direct relevant columns.

Ammended and normalised ERD is as below:
![alt text](<images/ERD ver2.png>)

### Feedback 2
Feedback received by an external developer


