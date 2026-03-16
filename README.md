# Task Manager API

A simple backend API built using **FastAPI** to manage tasks.

This project demonstrates the fundamentals of backend development, including creating API endpoints, handling HTTP requests, and returning JSON responses.

---

## Features

- Start a backend server using FastAPI
- Retrieve tasks using a GET API
- Create new tasks using a POST API
- Delete tasks using a DELETE API
- Interactive API testing using FastAPI's Swagger documentation

---

## Technologies Used

- Python
- FastAPI
- Uvicorn
- Pydantic

---

## Installation

Clone the repository and install dependencies.

bash
pip install -r requirements.txt

---
## Run the Server

Start the backend server using:

python -m uvicorn main:app --reload

The API will run at:

http://127.0.0.1:8000

---
## API Documentation

FastAPI automatically generates interactive API documentation.

Open:

http://127.0.0.1:8000/docs

You can test all endpoints directly from this interface.

---

## API Endpoints
Check Server Status
GET /

Response:

{"message": "Task Manager API is running"}

### Get All Tasks
GET /tasks

Example Response:

[
 {"id": 1,"title": "study DBMS","done": false},
  {"id": 2,"title": "finish CSV cleaner","done": true}
]

### Create a Task
POST /tasks

Example Request:

{"title": "prepare for internship applications"}

Example Response:

{"id": 3,"title": "prepare for internship applications",
"done": false}

### Delete a Task
DELETE /tasks/{task_id}

Example:

DELETE /tasks/2

Response:

{"message": "Task deleted"}

---

## Project Structure
task-manager-api
│
├── main.py
├── requirements.txt
└── README.md

---

## Future Improvements

Add task update functionality (PUT /tasks/{id})

Connect the API to a real database (MySQL/PostgreSQL)

Add user authentication

Add task completion status updates