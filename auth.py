from pydantic import BaseModel


class User(BaseModel):
    username: str
    password: str


class UserManager():
    @staticmethod
    def create_user(user: User):
        ...

    @staticmethod
    def delete_user(user: User):
        ...

    @staticmethod
    def get_user(username: str):
        ...


class Auth(object):

    def login(self, username, password):
        user = UserManager.get_user(username)
        if user is None:
            return False
        if user.password == password:
            return True
        return False

    def register(self, username, password):
        if UserManager.get_user(username) is not None:
            return False
        user = User(username=username, password=password)
        UserManager.create_user(user)

    def auth_check(self, username, password):
        if not self.login(username, password):
            return False
        return True
