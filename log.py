
from pydantic import BaseModel


class Log(BaseModel):
    log_id: int = None
    username: str
    timestamp: str


class Logger():
    @staticmethod
    def login(self, username):
        ...
    @staticmethod
    def enterHome(self, username):
        ...
    @staticmethod
    def exitHome(self, username):
        ...
    @staticmethod
    def klima(self, username, durum):
        ...
    @staticmethod
    def isik(self, username, durum):
        ...
    @staticmethod
    def pencere(self, username, durum):
        ...
    @staticmethod
    def get_logs(self):
        ...