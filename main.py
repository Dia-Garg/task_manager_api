from fastapi import FastAPI as fapi

app = fapi()

tasks = [{"id": 1, "title": "study DBMS", "done": False}, {"id": 2, "title": "finish CSV cleaner", "done": True}]

@app.get("/")
def home():
    return{"message": "Task Manager API is running"}

@app.get("/tasks")
def get_tasks():
    return tasks