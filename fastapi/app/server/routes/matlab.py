from fastapi import APIRouter, Body
from fastapi.encoders import jsonable_encoder

from server.database import (
    water_level_helper,
    MatlabDatabase,
)

from server.models.waterdata import (
    ErrorResponseModel,
    ResponseModel,
    WaterLevel,
    UpdateWaterLevel,
    MatlabData,
)

router = APIRouter()
database = MatlabDatabase(collection = "processed_water_data")

@router.post("/", response_description="Water data added into the database")
async def add_processed_data(water: MatlabData = Body(...)):
    water = jsonable_encoder(water)
    new_water = await database.add_water(water)
    return ResponseModel(new_water, "Water added successfully")