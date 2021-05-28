from enum import Enum
from fastapi import FastAPI

class namaUser(str,Enum):
    alfian = "Alfian Dimas"
    Komang = "Komang Tirtayasa"
    alucard = "AlucardML"
    
app = FastAPI()

@app.get("/user/{namauser}")

def get_model(nama_user:namaUser):
    if nama_user == nama_user.alfian:
        return {"namauser":nama_user, "message":"halo Alfian"}
    
    elif nama_user.value == "komang":
        return {"namauser":nama_user, "messages":"halo komang"}
    
    return {"namauser":nama_user, "message":"have Nice Day"}
