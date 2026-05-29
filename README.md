# TaskManager - Project Launch Instructions

## Requirements
Make sure you have installed:
- Docker
- Docker Compose

---

## Project Setup

1. Clone the repository:
```
git clone <repo-url>
cd TaskManager
```

2. Build and start the containers:
```
docker-compose up --build
```
---

## Access the Application

After startup, the service will be available at:
- API: http://localhost:8000
- Swagger UI: http://localhost:8000/docs

---

## Database (SQLite)

This project uses SQLite:
- No separate database container is required
- The database file is created automatically inside the project (e.g. app.db or database.db)

---

## API Endpoints

Create task:
POST /tasks

Get tasks:
GET /tasks
GET /tasks?status=done

Get task by id:
GET /tasks/{task_id}

Update task:
PATCH /tasks/{task_id}

Delete task:
DELETE /tasks/{task_id}

---

## Stop the project
```
docker-compose down
```

To remove containers and database data:
```
docker-compose down -v
```

---

## Notes
- FastAPI runs inside Docker
- Swagger documentation is available at /docs
- SQLite is used as embedded database (no external DB service required)
- If Alembic is used, migrations should be applied inside the backend container
