from pymongo import MongoClient

client = MongoClient(
    "mongodb+srv://bilal:Bo20yhCrC4KeyVY4xkhUhVO2wqotQ7zA@cluster0.csmai.mongodb.net/?retryWrites=true&w=majority")
db = client.eem


class HomeDB():
    instance = None

    def __call__(cls, *args, **kwargs):
        if cls.instance is None:
            cls.instance = super(HomeDB, cls).__call__(*args, **kwargs)
        return cls.instance

    def __init__(self):
        self.users = db["users"]
        self.logs = db["logs"]
        self.devices = db["devices"]
        self.alarms = db["alarms"]