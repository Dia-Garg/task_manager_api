from fastapi import FastAPI as fapi
from pydantic import BaseModel

app = fapi()

tasks = [{"id": 1, "title": "study DBMS", "done": False}, {"id": 2, "title": "finish CSV cleaner", "done": True}]

@app.get("/")
def home():
    return{"message": "Task Manager API is running"}

@app.get("/tasks")
def get_tasks():
    return tasks

class Task(BaseModel):
    title: str
    done: bool

@app.post("/tasks")
def create_task(task: Task):
    new_task={"id": len(tasks)+1, "title": task.title, "done": False}

    tasks.append(new_task)
    return new_task

@app.delete("/tasks/{task_id}")
def delete_task(task_id: int):
    for task in tasks:
        if task["id"]==task_id:
            tasks.remove(task)
            return {"message": "Task deleted"}
    return{"error": "Task not found"}

@app.put("/tasks/{task_id}")
def update_task(task_id: int, updated_task: Task):
    for task in tasks:
        if task["id"]== task_id:
            task["title"]= update_task.title
            task["done"]= update_task.done
            return{"message": "Task updated", "task": task}
    return{"error": "Task not found"}