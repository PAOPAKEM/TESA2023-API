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

@router.delete("/{id}", response_description="Water data deleted from the database")
async def delete_water_data(id: str):
    deleted_water = await database.delete_water(id)
    if deleted_water:
        return ResponseModel(
            "Water with ID: {} removed".format(id), "Water deleted successfully"
        )
    return ErrorResponseModel(
        "An error occurred", 404, "Water with id {0} doesn't exist".format(id)
    )
