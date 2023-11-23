from fastapi import APIRouter 
#fastapi_mqtt
from fastapi_mqtt.fastmqtt import FastMQTT
from fastapi_mqtt.config import MQTTConfig

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

# > Event Topic : tgr2023/BaanAndSuan/btn_evt
# > Command Topic : tgr2023/BaanAndSuan/cmd
### MQTT Client Settings here only
mqtt_config = MQTTConfig(host = "emqx",
    port= 1883,
    keepalive = 60,
    username="admin",
    password="weak_password")

CAPTURE_TOPIC = r"tgr2023/BaanAndSuan/cmd"
RECEIVE_TOPIC = r"tgr2023/BaanAndSuan/btn_evt"
### MQTT Client Settings here only

fast_mqtt = FastMQTT(config=mqtt_config)
router = APIRouter()
fast_mqtt.init_app(router)

### Routes

@router.get("/cap", response_description="Tell ESP32 to take a picture")
async def Take_a_picture_please():
    try:
        fast_mqtt.publish(CAPTURE_TOPIC, "TAKE A PICTURE!!!") #publishing mqtt topic
        return {"result": True, "message":"Picture Request Sent: " + CAPTURE_TOPIC}
    except Exception as e:
        return {"result": False, "message":str(e)}

### MQTT operation

@fast_mqtt.on_connect()
def connect(client, flags, rc, properties):
    fast_mqtt.client.subscribe("/mqtt") #subscribing mqtt topic
    print("Connected: ", client, flags, rc, properties)

@fast_mqtt.on_message()
async def message(client, topic, payload, qos, properties):
    print("Received message: ",topic, payload.decode(), qos, properties)

@fast_mqtt.subscribe("/TGR_44")
async def message_to_topic(client, topic, payload, qos, properties):
    print("Received message to specific topic: ", topic, payload.decode(), qos, properties)

@fast_mqtt.on_disconnect()
def disconnect(client, packet, exc=None):
    print("Disconnected")

@fast_mqtt.on_subscribe()
def subscribe(client, mid, qos, properties):
    print("subscribed", client, mid, qos, properties)



