from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

todos = []

class User(BaseModel):
    id: int
    title: str
    complete: bool

# CREATE
@app.post("/todos")
def create_todo(todo: User):
    todos.append(todo)
    return {
        "Message": "TODO created successfully",
        "Data": todo
    }

# READ
@app.get("/todos")
def get_all_todos():
    return todos


@app.get("/todos/{todo_id}")
def get_todo(todo_id: int):
    for todo in todos:
        if todo.id == todo_id:
            return todo
    return {"Error": "TODO not found"}


# UPDATE
@app.put("/todos/{todo_id}")
def update_todo(todo_id: int, updated_todo: User):
    for i in range(len(todos)):
        if todos[i].id == todo_id:
            todos[i] = updated_todo
            return {
                "Message": "TODO updated successfully",
                "Data": updated_todo
            }
    return {"Error": "TODO not found"}

# DELETE
@app.delete("/todos/{todo_id}")
def delete_todo(todo_id: int):
    for i in range(len(todos)):
        if todos[i].id == todo_id:
            deleted_todo = todos.pop(i)
            return {
                "Message": "TODO deleted successfully",
                "Data": deleted_todo
            }
    return {"Error": "TODO not found"}
