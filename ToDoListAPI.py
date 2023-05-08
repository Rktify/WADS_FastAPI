from fastapi import FastAPI, Path
from typing import Optional
from pydantic import BaseModel

app = FastAPI()

tasks = {
    1:{
        "title": "Assignment",
        "description": "WADS Assignment",
        "completed": True
    },
    2:{
        "title": "Quiz",
        "description": "WADS Quiz",
        "completed": False
    }
}

class Task(BaseModel):
    title:str
    description: str
    completed: bool

class Update(BaseModel):
    title: Optional[str] = None
    description: Optional[str] = None
    completed: Optional[bool] = None

@app.get("/")
def index():
    return {"Welcome":"Wilbert's todo app"}

@app.get("/tasks")
def listTasks():
    return tasks

@app.get("/get-task-by-title/{title}")
def getTask_by_title(title: str):
    for id in tasks:
        if tasks[id]["title"] == title:
            return tasks[id]
    return {"Error":"Task title was not found"}

@app.get("/get-task/{id}")
def getTask_by_id(id: int):
    if id not in tasks:
        return {"Error": "Task ID does not exist"}
    return tasks[id]

@app.post("/create-task/{id}")
def addTask(id: int, task: Task):
    if id in tasks:
        return{"Error": "Task id already exists"}
    tasks[id] = task
    return tasks[id]

@app.delete("/delete-task/{id}")
def deleteTask(id: int):
    if id not in tasks:
        return {"Error": "Task ID does not exist"}
    else:
        del tasks[id]
        return {"Successful": "Task has been deleted"}

@app.delete("/delete-task-by-title/{title}")
def deleteTask_by_title(title: str):
    for id in tasks:
        if tasks[id]["title"] == title:
            del tasks[id]
            return {"Successful": "Task has been deleted"}
    return {"Error": "Data does not exist"}

@app.put("/update-task/{id}")
def update_task(id: int, task: Update):
    if id not in tasks:
        return {"Error": "Task ID does not exist"}
    if task.title != None:
        tasks[id]["title"] = task.title
    if task.description != None:
        tasks[id]["description"] = task.description
    if task.completed != None:
        tasks[id]["completed"] = task.completed

    return tasks[id]