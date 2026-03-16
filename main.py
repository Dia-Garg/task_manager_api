from fastapi import FastAPI as fapi

app = fapi()

tasks = [{"id": 1, "title": "study DBMS", "done": False}, {"id": 2, "title": "finish CSV cleaner", "done": True}]

@app.get("/")
def home():
    return{"message": "Task Manager API is running"}

@app.get("/tasks")
def get_tasks():
    return tasks

from pydantic import BaseModel

class Task(BaseModel):
    title: str

@app.post("/tasks")
def create_task(task: Task):
    new_task={"id": len(tasks)+1, "title": task.title, "done": False}

    task.append(new_task)
    return new_task

@app.delete("/tasks/{task_id}")
def delete_task(task_id: int):
    for task in tasks:
        if task["id"]==task_id:
            tasks.remove(task)
            return {"message": "Task deleted"}
    return{"error": "Task not found"}