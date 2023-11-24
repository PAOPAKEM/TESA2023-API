from fastapi import APIRouter 
import json
from fastapi.encoders import jsonable_encoder
from fastapi_mqtt.fastmqtt import FastMQTT
from fastapi_mqtt.config import MQTTConfig
import time

from server.database import (
    water_level_helper,
    WaterDatabase,
)

from server.models.waterdata import (
    ErrorResponseModel,
    ResponseModel,
    WaterLevel,
    UpdateWaterLevel
)

database = WaterDatabase(collection = "water_level")

# > Event Topic : tgr2023/BaanAndSuan/btn_evt
# > Command Topic : tgr2023/BaanAndSuan/cmd
### MQTT Client Settings here only
mqtt_config = MQTTConfig(host = "emqx",
    port= 1883,
    keepalive = 60,
    username="admin",
    password="weak_password")

TESTERS_TOPIC = r"tgr2023/BaanAndSuan/vibe"
CAPTURE_TOPIC = r"tgr2023/BaanAndSuan/cmd"
RECEIVE_TOPIC = r"tgr2023/BaanAndSuan/evt"
### MQTT Client Settings here only

fast_mqtt = FastMQTT(config=mqtt_config)
router = APIRouter()
fast_mqtt.init_app(router)

### Routes for publish operations

@router.get("/capture", response_description="Tell ESP32 to take a picture")
async def Take_a_picture_please():
    data = json.dumps({"ID": 44, "cmd": "capture"})
    try:
        fast_mqtt.publish(CAPTURE_TOPIC, data) 
        return {"result": True, "message":"Request Sent: " + CAPTURE_TOPIC}
    except Exception as e:
        return {"result": False, "message":str(e)}

@router.get("/alivecheck", response_description="For checking if EMQX is alive")
async def check():
    try:
        fast_mqtt.publish(TESTERS_TOPIC, "vibecheck")
        return {"result": True, "message":"Request Sent: " + TESTERS_TOPIC}
    except Exception as e:
        return {"result": False, "message":str(e)}

### MQTT Subscribe operations

@fast_mqtt.subscribe(RECEIVE_TOPIC)
async def message_to_topic(client, topic, payload, qos, properties):
    print("Received message to specific topic: ", topic, payload.decode(), qos, properties)
    # TODO: Insert Data to Database
    try:
        payload = json.loads(payload.decode())
        water = WaterLevel(
            name = payload["ID"],
            timestamp= time.time(),
            waterlevel = float(payload["result"]),
        )
        water = jsonable_encoder(water)
        print("CODER:", water)
        new_water = await database.add_water(water)
        print("Added to database: ", new_water)
    except Exception as e:
        print("Error on adding to database: ", e)

### MQTT Status operation

@fast_mqtt.on_connect()
def connect(client, flags, rc, properties):
    fast_mqtt.client.subscribe("/mqtt") #subscribing mqtt topic
    print("Connected: ", client, flags, rc, properties)

@fast_mqtt.on_message()
async def message(client, topic, payload, qos, properties):
    print("Received message: ",topic, payload.decode(), qos, properties)

@fast_mqtt.on_disconnect()
def disconnect(client, packet, exc=None):
    print("Disconnected")

@fast_mqtt.on_subscribe()
def subscribe(client, mid, qos, properties):
    print("subscribed", client, mid, qos, properties)



