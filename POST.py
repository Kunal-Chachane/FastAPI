from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

# 1. PYDANTIC MODEL
# This defines the structure of data
# that we expect from the user.

class User(BaseModel):
    name: str
    age: int
    city: str

# 2. POST REQUEST
# POST is generally used to create/send data.
#
# URL:
# http://127.0.0.1:8000/users
#
# Data is sent in the request BODY, not in the URL.

@app.post("/users")
def create_user(user: User):
    return {
        "message": "User created successfully",
        "user": user
    }
