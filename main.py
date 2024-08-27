# THIS IS A SIMPLE PYTHON FILE FOR PROJECT 
from fastapi import FastAPI, HTTPException ,Depends,status
from pydantic import BaseModel , Field
from typing import Optional , Annotated
from Userclass import Userclass  
from package.Database import engine
from package.Database import SessionLocal
from package import models
from package.models import User  
from sqlalchemy.orm import Session
from sqlalchemy.orm import sessionmaker

models.Base.metadata.create_all(bind=engine)

def get_db():
    users_db = SessionLocal()
    try:
        yield users_db
    finally:
        users_db.close()
        
db_dependency = Annotated[Session, Depends(get_db)]
    
    
class UserCreate(BaseModel):
    username: str
    password: str = Field(min_length = 8)
    name: str
    email: str
    phone_number: str = Field(min_length = 11)
    

class LoginRequest(BaseModel):
    username: str 
    password: str = Field(min_length = 8)


#users_db = [User("johndoe","securepassword","John Doe","john.doe@example.com","123-456-7890"),
#            User("Abood","securepassword","Abood Aboody","Abood.Aboody@example.com","09123456789")]


app = FastAPI()

@app.get("/Show_Users")
async def read_all(users_db: db_dependency): 
    return users_db.query(User).all()


@app.post("/register_User",status_code=status.HTTP_201_CREATED)
def register(user: UserCreate, users_db : db_dependency):
    for data in users_db :
        if user.username == data.username:
            raise HTTPException(status_code=400, detail="Username already exists")
        
    new_user = Userclass(
        username=user.username,
        password=user.password,
        name=user.name,
        email=user.email,
        phone_number=user.phone_number
    )
    
    info = new_user.return_all_info()
    db_user = User(**info)
    users_db.add(db_user)
    users_db.commit()
    #users_db.append(new_user) 
    return {"message": "User registered successfully!"}



@app.post("/login/")
def login(login_request: LoginRequest, users_db : db_dependency):
    #Find User
    user = users_db.query(User).filter(User.username == login_request.username).first()
    #User not found
    if user is None:
        raise HTTPException(status_code=404, detail="User not found")
    #Extract User data
    login_user = Userclass(
        username=user.username,
        hash_pass=user.password,
        name=user.name,
        email=user.email,
        phone_number=user.phone_number
    )
    #check pass & make token
    token = login_user.login(login_request.password)
    if token:
        user.complete = True
        users_db.commit()
        return {"token": token}
    else:
        raise HTTPException(status_code=401, detail="Invalid password")
    
    
@app.get("/user/{username}/")
def get_user_info(username: str,users_db: db_dependency):
    #Find User
    user = users_db.query(User).filter(User.username == username).first()
    #User not found
    if user is None:
        raise HTTPException(status_code=404, detail="User not found")
    #show info
    if user.complete:
        return {
            "Username": user.username,
            "Name": user.name,
            "Email": user.email,
            "Phone Number": user.phone_number
        }
    else:
        return "User is not logged in."
    
@app.put("/logout/{username}/")
def logout(username: str,users_db: db_dependency):
    #Find User
    user = users_db.query(User).filter(User.username == username).first()
    #User not found
    if user is None:
        raise HTTPException(status_code=404, detail="User not found")
    #Logout
    user.complete = False 
    users_db.commit()
    return f"{user.name} Logout..."