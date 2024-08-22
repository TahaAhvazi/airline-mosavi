# THIS IS A SIMPLE PYTHON FILE FOR PROJECT 
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import Optional
from User import User  


class UserCreate(BaseModel):
    username: str
    password: str
    name: str
    email: str
    phone_number: str
    

class LoginRequest(BaseModel):
    username: str
    password: str


users_db = [User("johndoe","securepassword","John Doe","john.doe@example.com","123-456-7890"),
            User("Abood","securepassword","Abood Aboody","Abood.Aboody@example.com","09123456789")]


app = FastAPI()

@app.get("/Show_Users")
async def root(): 
    return users_db


@app.post("/register_User")
def register(user: UserCreate):
    for data in users_db :
        if user.username == data.username:
            raise HTTPException(status_code=400, detail="Username already exists")
        
    new_user = User(
        username=user.username,
        password=user.password,
        name=user.name,
        email=user.email,
        phone_number=user.phone_number
    )
    
    users_db.append(new_user) 
    return {"message": "User registered successfully!"}



@app.post("/login/")
def login(login_request: LoginRequest):
    #Find User
    for data in users_db :
        if login_request.username == data.username:
            user = data
            break
        else:
            user = None
    #User not found
    if user is None:
        raise HTTPException(status_code=404, detail="User not found")
    
    #check pass & make token
    token = user.login(login_request.password)
    if token:
        return {"token": token}
    else:
        raise HTTPException(status_code=401, detail="Invalid password")
    
    
@app.get("/user/{username}/")
def get_user_info(username: str):
    #Find User
    for data in users_db :
        if username == data.username:
            user = data
            break
        else:
            user = None
    #User not found
    if user is None:
        raise HTTPException(status_code=404, detail="User not found")
    #show info
    return user.display_info()
