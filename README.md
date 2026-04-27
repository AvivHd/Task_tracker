# Task Tracker API

A REST API for managing tasks built with FastAPI and SQLAlchemy, with a vanilla JS frontend.

## Features

- ✅ Create, read, update, and delete tasks
- ✅ Task prioritization and status tracking
- ✅ Due date management
- ✅ Health check endpoint
- ✅ Web UI accessible from the browser
- ✅ Built with FastAPI for high performance
- ✅ SQLAlchemy ORM for database abstraction
- ✅ PostgreSQL database support
- ✅ Test suite with pytest

## Technologies

- **FastAPI** — Modern web framework for building APIs
- **SQLAlchemy** — Python SQL toolkit and ORM
- **PostgreSQL** — Relational database
- **Pydantic** — Data validation using Python type annotations
- **Uvicorn** — ASGI web server
- **pytest** — Testing framework

## Project Structure

```
task_tracker/
├── app/
│   ├── main.py           # FastAPI app initialization
│   ├── database.py       # Database configuration and session management
│   ├── models.py         # SQLAlchemy ORM models
│   ├── schemas.py        # Pydantic request/response schemas
│   └── routers/
│       └── tasks.py      # Task API endpoints
├── static/
│   └── index.html        # Frontend UI
├── tests/
│   └── test_tasks.py     # Tests
├── requirements.txt      # Project dependencies
└── README.md             # This file
```

## Installation

### Running with Docker (Recommended)

The easiest way to run the project:

```bash
docker compose up --build
```

The API will be available at `http://localhost:8000`
The frontend UI will be available at `http://localhost:8000/static/index.html`

### Running Locally

1. **Clone the repository** (or navigate to the project directory)
   ```bash
   cd task_tracker
   ```

2. **Create and activate a virtual environment**
   ```bash
   python -m venv .venv
   .venv\Scripts\activate  # On Windows
   # or
   source .venv/bin/activate  # On macOS/Linux
   ```

3. **Install dependencies**
   ```bash
   .venv\Scripts\python.exe -m pip install -r requirements.txt
   ```

4. **Configure the database**
   - Set the DATABASE_URL environment variable, or leave it as is to use the SQLite fallback for local development.

## Running the Application

Start the development server:
```bash
uvicorn app.main:app --reload
```

The API will be available at `http://localhost:8000`

Access the interactive API documentation:
- Swagger UI: `http://localhost:8000/docs`
- ReDoc: `http://localhost:8000/redoc`

## API Endpoints

### Health Check
- **GET** `/health` — Returns server status

### Tasks

- **POST** `/tasks/` — Create a new task
  ```json
  {
    "title": "Task title",
    "description": "Optional description",
    "priority": 1,
    "due_date": "2026-04-20T10:00:00"
  }
  ```

- **GET** `/tasks` — Get all tasks

- **GET** `/tasks/{task_id}` — Get a specific task by ID

- **PUT** `/tasks/{task_id}` — Update a task
  ```json
  {
    "status": "in_progress",
    "priority": "medium"
  }
  ```

- **DELETE** `/tasks/{task_id}` — Delete a task

## Task Model

| Field | Type | Description |
|-------|------|-------------|
| `id` | Integer | Primary key (auto-generated) |
| `title` | String | Task title (required) |
| `description` | String | Task description (optional) |
| `status` | String | Task status (default: "open") |
| `priority` | Integer | Priority level (default: 3) |
| `due_date` | DateTime | Task due date (optional) |
| `created_at` | DateTime | Creation timestamp (auto-generated) |

## Testing

Run the test suite:
```bash
pytest tests/
```

Run tests with verbose output:
```bash
pytest tests/ -v
```

## Database

The application automatically creates all required tables on startup if they don't already exist.
