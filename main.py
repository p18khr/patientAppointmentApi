from fastapi import FastAPI

app = FastAPI()

from fastapi.responses import JSONResponse


@app.get("/patient")
async def getPatient():
    patient = [{
        "Name":"Manoj",
        "Age":43
    }]
    return JSONResponse(patient)


@app.get("/hello/{name}")
async def say_hello(name: str):
    return {"message": f"Hello {name}"}
