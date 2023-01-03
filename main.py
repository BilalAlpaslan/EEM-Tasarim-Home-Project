from fastapi import Depends, FastAPI, Header
from fastapi.exceptions import HTTPException

from db import HomeDB
from auth import Auth
from kontrol import Kontrol

app = FastAPI()
db = HomeDB()


async def verify_key(user: str = Header(), password: str = Header(...)):
    if not Auth.auth_check(user, password):
        raise HTTPException(status_code=401, detail="Invalid credentials")


@app.get("/isik/{durum}" , dependencies=[Depends(verify_key)])
def isik(durum: int):
    Kontrol.isikKontrol(durum)
    


@app.get("/kapi/{durum}", dependencies=[Depends(verify_key)])
def kapi(durum: int):
    Kontrol.kapiKontrol(durum)


@app.get("/pencere/{durum}", dependencies=[Depends(verify_key)])
def pencere(durum: int):
    Kontrol.pencereKontrol(durum)


@app.get("/klima/{durum}", dependencies=[Depends(verify_key)])
def klima(durum: int):
    Kontrol.klimaKontrol(durum)


@app.get("/check", dependencies=[Depends(verify_key)])
def check():
    return {"message": "Success"}


@app.get("/register")
def register(home_key: str, username: str, password: str):
    if home_key != "1234":
        raise HTTPException(status_code=401, detail="Invalid credentials")
    user = Auth.register(username, password)
    if not user:
        raise HTTPException(status_code=401, detail="Username already exists")
    return user


@app.get("/getLog")
def get_logs():
    ...



if __name__ == "__main__":
    import uvicorn
    uvicorn.run('main:app', port=8000, reload=True)
