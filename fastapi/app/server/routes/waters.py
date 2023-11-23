from fastapi import APIRouter, Body
from fastapi.encoders import jsonable_encoder
from time import time

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
database = WaterDatabase(collection = "water_level")

# Get all water
@router.get("/", response_description="Waters retrieved")
async def get_waters():
    waters = await database.retrieve_all_waters()
    if waters:
        return ResponseModel(waters, "Waters data retrieved successfully")
    return ResponseModel(waters, "Empty list returned")

# Get 1 water
@router.get("/{id}", response_description="Waters retrieved")
async def get_water(id):
    waters = await database.retrieve_water(id)
    if waters:
        return ResponseModel(waters, "Waters data retrieved successfully")
    return ErrorResponseModel("An error occurred.", 404, "Student doesn't exist.")

# Get n latest wate
@router.get("/latest-add/{n}", response_description="Lastest n retrieved")
async def get_latest_add(n):
    waters = await database.retrieve_latest(n)
    if waters:
        return ResponseModel(waters, "n water data retrieved successfully")
    return ResponseModel(waters, "Empty list returned")

# Get n latest wate
@router.get("/latest-time/{n}", response_description="Lastest n retrieved")
async def get_latest_time(n):
    waters = await database.retrieve_latest(n, value = "timestamp")
    if waters:
        return ResponseModel(waters, "n water data retrieved successfully")
    return ResponseModel(waters, "Empty list returned")

# Add water data by hand
# we generate time stamp for the user, no need to worry
@router.post("/", response_description="Water data added into the database")
async def add_water_data_manually(water: WaterLevel = Body(...)):
    water.timestamp = time()
    water = jsonable_encoder(water)
    new_water = await database.add_water(water)
    return ResponseModel(new_water, "Water added successfully")

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

# @router.get("/{id}", response_description="Water data retrieved")
# async def get_water_data(id):
#     water = await retrieve_water(id)
#     if water:
#         return ResponseModel(water, "Water data retrieved successfully")
#     return ErrorResponseModel("An error occurred.", 404, "Student doesn't exist.")

# @router.put("/{id}")
# async def update_water_data(id: str, req: UpdateWaterModel = Body(...)):
#     req = {k: v for k, v in req.dict().items() if v is not None}
#     updated_water = await update_water(id, req)
#     if updated_water:
#         return ResponseModel(
#             "Water with ID: {} name update is successful".format(id),
#             "Water name updated successfully",
#         )
#     return ErrorResponseModel(
#         "An error occurred",
#         404,
#         "There was an error updating the water data.",
#     )

# @router.delete("/{id}", response_description="Water data deleted from the database")
# async def delete_water_data(id: str):
#     deleted_water = await delete_water(id)
#     if deleted_water:
#         return ResponseModel(
#             "Water with ID: {} removed".format(id), "Water deleted successfully"
#         )
#     return ErrorResponseModel(
#         "An error occurred", 404, "Water with id {0} doesn't exist".format(id)
#     )

