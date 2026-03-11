# Task Manager API

A simple backend API built with FastAPI to manage tasks.

This project demonstrates basic backend concepts such as API endpoints, HTTP methods, and JSON responses.

---

## Features

- Start a backend server using FastAPI
- Retrieve tasks using a GET API
- Interactive API documentation using Swagger UI
- Simple task storage using Python dictionaries

---

## Technologies Used

- Python
- FastAPI
- Uvicorn

---

## Installation

Install dependencies:
pip install -r requirements.txt

---

## Run the Server

Start the backend server:
python -m uvicorn main:app --reload

The API will run at:
https://127.0.0.1:8000

---

## API Documentation

FastAPI automatically generates interactive API documentation.

Open:
https://127.0.0.1:8000/docs

You can test the API directly from the browser. 

---

## Example Endpoints

### Get Server Status

GET/
Response:
{"message": "Task Manager API is running"}

### Get All Tasks

GET/tasks

Example Response:
[
    {"id": 1, "title": "study DBMS", "done": False}, {"id": 2, "title": "finish CSV cleaner", "done": True}
    ]

--- 

## Future Improvements

- Add API to create tasks
- Add API to delete tasks
- Connect the API to a database
- Add user authentication 

## Project Goal

This project is a beginner backend API built using FastAPI.  
It demonstrates how to create a server, define API endpoints, and return JSON responses.

The API currently supports retrieving tasks and will be extended to support creating and deleting tasks.