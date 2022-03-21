from datetime import datetime as dt
import string
from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

class sensors(BaseModel):
    sensor_1:str
    sensor_2:str

class UltrasonicSensors(BaseModel):
    date : str
    local_time : str    # In IST
    sensors : sensors

@app.get("/")
def message():
    print("---Log message --> Message function is executed---")
    return "Success 200"

@app.post("/sensors")
def sensor_status(sensors: UltrasonicSensors):
    print(sensors)