#import package - fastapi
from fastapi import FastAPI, HTTPException, Header
import pandas as pd

#membuat instance/object FastAPI
app = FastAPI()

#memubat API key
api_key = "secret123"

#rules
#endpoint -> url yang akan digunakan oleh client
#HTTP function (get,put,post,delete)
#alamat url

#define endpoint -> endpoint home
@app.get("/")
def getData(kunci: str = Header(None)):
    # do some process

    # validate kunci apakah sama dengan api key
    # cek ketersediaan kunci dalam request
    # cek kesamaan value kunci dengan api key
    if kunci == None or kunci != api_key:
        #kunci salah / tidak ada
        #return error
        raise HTTPException(status_code=401, detail="Anda tidak punya aksess ke endpoint ini")

    # return hasil process (berupa dict/json)
    return {
        "message": "This is my API"
    }

@app.get("/data")
def getDataCSV():

    #retrive data form csv
    df = pd.read_csv("data.csv")

    #do some process

    #sebelum return, convert DataFrame to Dictionary
    df = df.to_dict(orient = "records")

    return df

@app.get("/data/{name}")
def getFilterData(name: str):
    df = pd.read_csv("data.csv")

    filter = df[df['nama'] == name]

    return filter.to_dict(orient="records")






# menjalankan script di terminal
# uvicorn [nama_file]:[nama_instance] --reload
# uvicorn main:app --reload

# mematikan uvicorn
# ctrl + c

# localhost atau 127.0.0.1 -> alamat default ketika menjalankan uvicorn di komputer sendiri (local)
# :8000 -> nomor port default dari uvicorn

# pengujian api
# browser -> hanya untuk http function get
# documentation ->
# - sebagai informasi/buku manual dari API yang sudah dibuat
# - tempat menguji api -> bisa untuk semua http function

# fastapi -> include docs -> Swagger -> akses: endpoint/docs
# opsiL install Postman -> software API documentation