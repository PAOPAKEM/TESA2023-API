from fastapi import FastAPI
from server.routes.waters import router as WaterRouter
from server.mqtt.sensor_data import router as MqttRouter
from server.routes.matlab import router as matlab

from server.models.waterdata import ResponseModel

app = FastAPI()

####router api part

app.include_router(MqttRouter, tags=["MQTT"],prefix="/mqtt")
app.include_router(WaterRouter, tags=["Water"], prefix="/water")
app.include_router(matlab, tags=["Water"], prefix="/water")

# hello motherfucker
@app.get("/", response_description="Send hello motherfucker", tags = ["Root"])
async def send_dummy_data():
    return ResponseModel("Hello Motherfucker", "Mother fucker hello'ed")