from typing import Optional
from pydantic import BaseModel, Field
from typing import List, Optional
import time

def ResponseModel(data, message):
    return {
        "data": [data],
        "code": 200,
        "message": message,
    }

def ErrorResponseModel(error, code, message):
    return {"error": error, "code": code, "message": message}

# Water level, for storing water level data into database
# such data should be retrieved from mqtt directly

class UpdateWaterLevel(BaseModel):
    name: Optional[str]
    timestamp: Optional[float]
    waterlevel: Optional[float]

    class Config:
        schema_extra = {
            "example": {
                "name": "Moscow",
                "timestamp": 1594819641.9622827,
                "waterlevel": 87.1,
            }
        }

class WaterLevel(BaseModel):
    name: str = Field(...)
    timestamp: float = Field(default=time.time())
    waterlevel: float = Field(..., gt=0)

    class Config:
        schema_extra = {
            "example": {
                "name": "Moscow",
                "timestamp": 1594819641.9622827,
                "waterlevel": 87.1,
            }
        }

## Matlab data

class MatlabData(BaseModel):
    data: List[float] = Field(...)