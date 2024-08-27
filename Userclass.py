import bcrypt
import jwt
import datetime

class Userclass:
    username: str
    password: str
    hash_pass : str
    name: str
    email: str
    phone_number: str 
    SECRET_KEY = 'secret_key' 
    

    def __init__(self, username=None, password=None,hash_pass=None , name=None, email=None, phone_number=None):
        self.username = username
        self.__password_hash = self.hash_password(password)
        self.hash_pass = hash_pass
        self.name = name
        self.email = email
        self.phone_number = phone_number
        self.is_logged_in = False
        
    def return_all_info(self): 
        return {
                "username": self.username,
                "password": self.__password_hash ,
                "name": self.name,
                "email": self.email,
                "phone_number": self.phone_number
            }

    def hash_password(self, password):
        if password == None:
            return None
        else:
            return bcrypt.hashpw(password.encode(), bcrypt.gensalt())

    def check_password(self, password):
        
        return bcrypt.checkpw(password.encode(), self.hash_pass)

    def create_token(self):
        
        payload = {
            'username': self.username,
            'exp': datetime.datetime.utcnow() + datetime.timedelta(hours=1)  
        }
        return jwt.encode(payload, self.SECRET_KEY, algorithm='HS256')
        

    def login(self, password):
       
        if self.check_password(password):
            
            return self.create_token()
        return None


 