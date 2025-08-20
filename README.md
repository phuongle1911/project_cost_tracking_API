- add error handler database message
- add error handler for wrong data type for date
- add more error handling for another error codes
- fix post request in project personnel, still post new data even violate unique constraint. However, this works fine with Patch request

# Project Cost Tracking API Server

## About the project
This project is for setting up and recording project costs during project delivery phase. Based on that, Project Manager can keep track of costs at any time during project delivery. 

## Feedbacks 

### Feedback 1
Feedback received by Aamod on below initial diagram:
- There's a one to many relationship from projects to "incurred costs", and also from the junction table "cost_allocation" to "incurred costs". Maybe avoid the junction table connection. If you do plan to keep the connection:
  
- Have a separate PK in the junction table
It works as a FK in the "incurred costs" table.

- The concept of "Incurred costs" and "Cost Allocation" seems redundant.
responsible_staff in "incurred costs" table, is it supposed to track staff? If so, a good idea is to create a staffs table and link it (normalisation would help here).

- You have "project manager" as well. So maybe project manager can link to "staffs" table?

- Because you have project start, completion dates, you could also add a "status" attribute to the "projects" table that has (active, completed, cancelled, or something similar).
![alt text](<images/ERD ver1.png>)

**Actions**:
- Remove project_cost_summary, cost allocation and cost_codes tables
- Normalise by creating a staffs table, and a conjunction table "project_personnel" connecting projects and staffs tables. 
Normalise costs table containing only directly relevant columns.

Ammended and normalised ERD is as below:
![alt text](<images/ERD ver2.png>)


