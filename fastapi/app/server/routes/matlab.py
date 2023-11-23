from fastapi import APIRouter, Body
from fastapi.encoders import jsonable_encoder

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

router = APIRouter()
database = WaterDatabase(collection = "processed_water_data")