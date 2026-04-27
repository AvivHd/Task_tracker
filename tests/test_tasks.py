from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)

# send a POST request with a title
# check the status code is 200
# check the returned data has the right title
def test_create_task():
    response = client.post("/tasks/", json={"title": "Test task",
                                 "description": "This is a test task",
                                 "priority": "medium",
                                  "due_date": "31/12/2024, 23:59"})
    assert response.status_code == 200
    assert response.json()["title"] == "Test task"
    assert response.json()["due_date"] == "31/12/2024, 23:59"

# send a GET request
# check the status code is 200
# check the response is a list
def test_get_tasks():
    response = client.get("/tasks/")
    assert response.status_code == 200
    assert isinstance(response.json(), list)

# send a GET request for an id that doesn't exist
# check the status code is 404
def test_get_task_not_found():
    response = client.get("/tasks/999999")
    assert response.status_code == 404

def test_delete_task():
    response = client.post("/tasks/", json={"title": "Task to delete"})
    assert response.status_code == 200
    task_id = response.json()["id"]
    delete_response = client.delete(f"/tasks/{task_id}")
    assert delete_response.status_code == 204
    get_response = client.get(f"/tasks/{task_id}")
    assert get_response.status_code == 404

def test_update_task():
    response = client.post("/tasks/", json={"title": "Task to update"})
    assert response.status_code == 200
    task_id = response.json()["id"]
    update_task = {"description": "Updated the task",
                   "status": "in_progress"}
    update_task_response = client.put(f"/tasks/{task_id}", json=update_task)

    assert update_task_response.status_code == 200
    assert update_task_response.json()["description"] == "Updated the task"
    assert update_task_response.json()["status"] == "in_progress"