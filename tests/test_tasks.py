from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)

# send a POST request with a title
# check the status code is 200
# check the returned data has the right title
def test_create_task():
    response = client.post("/tasks/", json={
        "title": "Test task",
        "description": "This is a test task",
        "priority": "medium",
        "due_date": "2024-12-31T23:59:00"
    })
    assert response.status_code == 200
    assert response.json()["title"] == "Test task"

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

# Test for creating a task with an empty title (should return 422)
def test_create_task_empty_title():
    response = client.post("/tasks/", json={"title": ""})
    assert response.status_code == 422

# Test for search (GET /tasks/?search=something)
def test_search_tasks():
    # Create a task to search for
    client.post("/tasks/", json={"title": "Unique Search Task"})
    response = client.get("/tasks/?search=Unique")
    assert response.status_code == 200
    tasks = response.json()
    assert any(task["title"] == "Unique Search Task" for task in tasks)

# Test for filtering by status and priority
def test_filter_status_task():
    # Create tasks with different statuses and priorities
    client.post("/tasks/", json={"title": "Open Task", "priority": "high"})
    client.post("/tasks/", json={"title": "In Progress Task", "priority": "medium"})
    client.post("/tasks/", json={"title": "Done Task", "priority": "low"})

    response = client.get("/tasks/?status=open&priority=high")
    assert response.status_code == 200
    tasks = response.json()
    assert all(task["status"] == "open" and task["priority"] == "high" for task in tasks)
    assert tasks[0]["title"] == "Open Task"

# Test for updating a task that doesn't exist (should return 404)
def test_update_task_not_found():
    response = client.put("/tasks/999999", json={"description": "Trying to update a non-existent task"})
    assert response.status_code == 404