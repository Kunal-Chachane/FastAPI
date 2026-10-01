from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()


class User(BaseModel):
    name: str
    age: int


users = []


# CREATE
@app.post("/users")
def create_user(user: User):
    users.append(user)
    return user


# READ
@app.get("/users")
def get_users():
    return users


# UPDATE
@app.put("/users/{index}")
def update_user(index: int, user: User):
    users[index] = user
    return user


# DELETE
@app.delete("/users/{index}")
def delete_user(index: int):
    users.pop(index)
    return {"message": "User deleted"}
