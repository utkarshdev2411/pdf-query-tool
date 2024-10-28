# app.py
from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def read_root():
    print("Server is running")
    return {"message": "Server is running"}


    
# uvicorn app:app --reload