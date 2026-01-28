
from fastapi import FastAPI

app = FastAPI()

@app.get("/health")
def read_root():
    return {"message": "ok"}

@app.get("/")
def read_root():
    return {"message": "Hello, world!"}