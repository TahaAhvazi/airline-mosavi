import bcrypt
import jwt
import datetime

class User:
    username: str
    password: str
    name: str
    email: str
    phone_number: str 
    SECRET_KEY = 'secret_key' 
    

    def __init__(self, username, password, name, email, phone_number):
        self.username = username
        self.__password_hash = self.hash_password(password)
        self.name = name
        self.email = email
        self.phone_number = phone_number
        self.is_logged_in = False

    def hash_password(self, password):
        
        return bcrypt.hashpw(password.encode(), bcrypt.gensalt())

    def check_password(self, password):
        
        return bcrypt.checkpw(password.encode(), self.__password_hash)

    def create_token(self):
        
        payload = {
            'username': self.username,
            'exp': datetime.datetime.utcnow() + datetime.timedelta(hours=1)  
        }
        return jwt.encode(payload, self.SECRET_KEY, algorithm='HS256')

    def login(self, password):
       
        if self.check_password(password):
            self.is_logged_in = True
            return self.create_token()
        return None

    def logout(self):
        
        self.is_logged_in = False

    def display_info(self):
        
        if self.is_logged_in:
            return {
                "Username": self.username,
                "Name": self.name,
                "Email": self.email,
                "Phone Number": self.phone_number
            }
        else:
            return "User is not logged in."