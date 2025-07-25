from fastapi import FastAPI, HTTPException

app = FastAPI()


@app.get("/")
def default():
    return {"message":"this the home page"}




