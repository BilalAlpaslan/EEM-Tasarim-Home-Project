from fastapi import FastAPI
app = FastAPI()


@app.get("/isik/{durum}")
def isik(durum: int):
    ...

@app.get("/kapi/{durum}")
def kapi(durum: int):
    ...

@app.get("/pencere/{durum}")
def pencere(durum: int):
    ...

@app.get("/klima/{durum}")
def klima(durum: int):
    ...

@app.get("/login/{username}")
def login(username: str):
    ...
    
@app.get("/register/{username}")
def register(username: str):
    ...