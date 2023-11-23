from fastapi import APIRouter, Body
from fastapi.encoders import jsonable_encoder

from server.database import (
    MatlabDatabase,
)

from server.models.waterdata import (
    ErrorResponseModel,
    ResponseModel,
    MatlabData,
)

router = APIRouter()
database = MatlabDatabase(collection = "processed_water_data")

@router.get("/{n}", response_description="Water data retrieved")
async def get_n_latest_processed_data(n):
    waters = await database.retrieve_latest(n)
    if waters:
        return ResponseModel(waters, "Water data retrieved successfully")
    return ResponseModel(waters, "Empty list returned")

@router.post("/", response_description="Water data added into the database")
async def add_processed_data(water: MatlabData = Body(...)):
    water = jsonable_encoder(water)
    new_water = await database.add_water(water)
    return ResponseModel(new_water, "Matlab Processed Data added successfully")