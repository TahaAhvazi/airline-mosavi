from package.Database import Base
from sqlalchemy import Column , Integer ,String , Boolean

class User(Base):
    __tablename__ = 'Users'
    
    username = Column(String, primary_key=True)
    password= Column(String)
    name= Column(String)
    email= Column(String)
    phone_number= Column(String)
    complete = Column(Boolean , default=False)