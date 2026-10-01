from fastapi import FastAPI

app = FastAPI()

# 1. BASIC ROUTE

@app.get("/about")
def about():
    # This route does not take any parameter
    return {
        "message": "This is About Page"
    }
  
# 2. QUERY PARAMETER
# name: str = None
# str  -> name should be a string
# None -> parameter is optional

@app.get("/users")
def get_users(name: str = None):

    return {
        "Name": name
    }

# 3. MULTIPLE QUERY PARAMETERS
# We can have more than one query parameter.
# ? -> starts query parameters
# & -> separates multiple parameters

@app.get("/user-info")
def user_info(name: str = None, age: int = None):

    return {
        "Name": name,
        "Age": age
    }



