

def test_get_projects_returns_empty_list(client):
  response = client.get("/projects")
  assert response.status_code == 200
  assert response.get_json() == []

def test_create_project_success(client):
  new_project = {
    "name":"ANZ commercial application development",
    "client":"ANZ",
    "location":"Sydney",
    "start_date":"2025-01-10",
    "estimate_completion_date'":"2025-06-15",
    "status":"Active",
    "contract_value":60000,
    "budget":40000
  }
  
  response = client.post("/projects", json = new_project)
  assert response.status_code == 201
  project = response.get_json()
  assert 'name' in project
  assert project['name'] == "ANZ commercial application development"

def test_create_project_invalid_text(client):
  new_project = {
    "name":"ANZ commercial application development",
    "client":"AN",
    "location":"Sydney",
    "start_date":"2025-01-10",
    "estimate_completion_date'":"2025-06-15",
    "status":"Active",
    "contract_value":60000,
    "budget":40000
  }

  response = client.post("/projects", json = new_project)
  assert response.status_code == 400
  message = response.get_json()
  assert "client" in message
  assert message['client'] == ["Invalid input! String is too short!"]


def test_get_project_success(client):
  response = client.get('/projects')
  assert response.status_code == 200
  data = response.get_json()
  assert isinstance(data,list)

# def test_update_project_success(client):
#   new_project = {
#     "name":"ANZ commercial application development",
#     "client":"ANZ",
#     "location":"Sydney",
#     "start_date":"2025-01-10",
#     "estimate_completion_date'":"2025-06-15",
#     "status":"Active",
#     "contract_value":60000,
#     "budget":40000
#   }

#   response = client.post('/projects', json = new_project)
#   project = response.get_json()
#   project_id = project["id"]

