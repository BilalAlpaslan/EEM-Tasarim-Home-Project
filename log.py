
from typing import List
from pydantic import BaseModel
import time

from db import HomeDB


db = HomeDB()


class Log(BaseModel):
    log_id: int = None
    username: str
    text: str
    logtype: str = None
    timestamp: str


class Logger():
    @staticmethod
    def saveLog(username, text, logtype):
        last_log = db.logs.find_one(sort=[("log_id", -1)])
        last_log_id = last_log.log_id if last_log else 0
        timestamp = time.time()
        log = Log(log_id=last_log_id + 1, username=username,
                  text=text, timestamp=timestamp, logtype=logtype)
        db.logs.insert_one(log.dict())

    @staticmethod
    def login(username):
        Logger.saveLog(username, "Login", "login")
        
    @staticmethod
    def register(username):
        Logger.saveLog(username, "Register", "register")

    @staticmethod
    def enterHome(username):
        Logger.saveLog(username, "Enter Home", "kapi")

    @staticmethod
    def exitHome(username):
        Logger.saveLog(username, "Exit Home", "kapi")

    @staticmethod
    def klima(username, durum):
        Logger.saveLog(username, "Klima " + str(durum), "klima")

    @staticmethod
    def isik(username, durum):
        Logger.saveLog(username, "Isik " + str(durum), "isik")

    @staticmethod
    def pencere(username, durum):
        Logger.saveLog(username, "Pencere " + str(durum), "pencere")

    @staticmethod
    def get_logs(type='all') -> List[Log]:
        if type != 'all':
            logs = db.logs.find({"type": type})
        else:
            logs = db.logs.find({})
        return [Log(**log) for log in logs]
