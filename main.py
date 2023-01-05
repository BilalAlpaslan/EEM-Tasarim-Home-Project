from fastapi import Depends, FastAPI, Header
from fastapi.middleware.cors import CORSMiddleware
from fastapi.exceptions import HTTPException

from db import HomeDB
from auth import Auth
from kontrol import Kontrol
from log import Logger

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


db = HomeDB()


async def verify_key(user: str = Header(), password: str = Header(...)):
    if not Auth.auth_check(user, password):
        raise HTTPException(status_code=401, detail="Invalid credentials")


@app.get("/isik/{durum}" , dependencies=[Depends(verify_key)])
def isik(durum: int, user: str = Header(...)):
    Kontrol.isikKontrol(durum)
    Logger.isik(user, durum)



@app.get("/kapi/{durum}", dependencies=[Depends(verify_key)])
def kapi(durum: int, user: str = Header(...)):
    Kontrol.kapiKontrol(durum)
    if durum == 1:
        Logger.enterHome(user)
    else:
        Logger.exitHome(user)


@app.get("/pencere/{durum}", dependencies=[Depends(verify_key)])
def pencere(durum: int, user: str = Header(...)):
    Kontrol.pencereKontrol(durum)
    Logger.pencere(user, durum)


@app.get("/klima/{durum}", dependencies=[Depends(verify_key)])
def klima(durum: int, user: str = Header(...)):
    Kontrol.klimaKontrol(durum)
    Logger.klima(user, durum)


@app.get("/check", dependencies=[Depends(verify_key)])
def check(user: str = Header(...)):
    Logger.login(user)
    return {"message": "Success"}


@app.get("/register")
def register(home_key: str, username: str, password: str):
    if home_key != "1234":
        raise HTTPException(status_code=401, detail="Invalid credentials")
    user = Auth.register(username, password)
    if not user:
        raise HTTPException(status_code=401, detail="Username already exists")
    Logger.register(username)
    return user


@app.get("/getLog/{type}")
def get_logs(type: str = 'all'):
    return Logger.get_logs(type)



if __name__ == "__main__":
    import uvicorn
    uvicorn.run('main:app', port=8000, reload=True)
