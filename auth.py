from pydantic import BaseModel

from db import HomeDB


db = HomeDB()

class User(BaseModel):
    user_id: int = None
    username: str
    password: str


class UserManager():
    @staticmethod
    def create_user(user: User):
        last_user = db.users.find_one(sort=[("user_id", -1)])
        last_id = last_user["user_id"] if last_user else 0
        user.user_id = last_id + 1
        db.users.insert_one(user.dict())
        return user

    @staticmethod
    def delete_user(user: User):
        db.users.delete_one({"user_id": user.user_id})

    @staticmethod
    def get_user(username: str):
        user = db.users.find_one({"username": username})
        if user:
            return User(**user)
        return None


class Auth():
    @staticmethod
    def login(username, password):
        user = UserManager.get_user(username)
        if user is None:
            return False
        if user.password == password:
            return True
        return False

    @staticmethod
    def register(username, password):
        if UserManager.get_user(username) is not None:
            return False
        user = User(username=username, password=password)
        return UserManager.create_user(user)
        

    @staticmethod
    def auth_check(username, password):
        if not Auth.login(username, password):
            return False
        return True
