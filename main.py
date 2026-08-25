from fastapi import FastAPI
app=FastAPI()
@app.get("/")

def read_root():
    return {"message":"welcome to fastapi"}
@app.get("/name")

def read_name():
    return {"name":"vijaya"}
             
