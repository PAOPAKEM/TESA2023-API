import motor.motor_asyncio
from bson.objectid import ObjectId

def water_level_helper(water) -> dict:
    return {
        "id": str(water["_id"]),
        "name": water["name"],
        "timestamp": water["timestamp"],
        "waterlevel": water["waterlevel"],
    }

class WaterDatabase():
    def __init__(self, collection:str, host:str = "mongoDB", port:int = "27017", auth_user:str = "admin", auth_pass:str = "hellboy_000"):
        self.auth_user = auth_user
        self.auth_pass = auth_pass
        self.host = host
        self.port = port
        self.collection = collection

        self._client = motor.motor_asyncio.AsyncIOMotorClient(f"mongodb://{self.auth_user}:{self.auth_pass}@{host}:{port}")
        self._db = self._client.water_data
        self._collection = self._db.get_collection(self.collection)

    async def add_water(self, water_data: dict) -> dict:
        water = await self._collection.insert_one(water_data)
        new_water = await self._collection.find_one({"_id": water.inserted_id})
        return water_level_helper(new_water)

    async def retrieve_water(self, id: str) -> dict:
        water = await self._collection.find_one({"_id": ObjectId(id)})
        if water:
            return water_level_helper(water)
    
    async def delete_water(self, id: str):
        water = await self._collection.find_one({"_id": ObjectId(id)})
        if water:
            await self._collection.delete_one({"_id": ObjectId(id)})
            return True

    # order -1 lastest first, 1 oldest first
    # value ($natural = ID)(timestamp = timestamp) 
    async def retrieve_latest(self, n: int, order: int = -1, value: str = "$natural"):
        waters = []
        async for water in self._collection.find().sort([(value, order )]).limit(int(n)):
            waters.append(water_level_helper(water))
        return waters
    
    async def retrieve_all_waters(self):
        waters = []
        async for water in self._collection.find():
            waters.append(water_level_helper(water))
        return waters
    
    


### EXTERN

# def water_helper(water) -> dict:
#     return {
#         "id": str(water["_id"]),
#         "name": water["name"],
#         "year": water["year"],
#         "month": water["month"],
#         "date": water["date"],
#         "waterfront": water["waterfront"],
#         "waterback": water["waterback"],
#         "waterdrain": water["waterdrain"],
#     }

# def cubic_water_helper(water) -> dict:
#     return {
#         "id": str(water["_id"]),
#         "timestamp": water["timestamp"],
#         "water_height": water["water_height"],
#         "water_cubic": water["water_cubic"],
#     }

# MONGO_DETAILS = "mongodb://admin:hellboy_000@mongoDB:27017"

# client = motor.motor_asyncio.AsyncIOMotorClient(MONGO_DETAILS)

# database = client.water_data

# water_collection = database.get_collection("waters_collection")

# Retrieve all waters present in the database
# async def retrieve_waters():
#     waters = []
#     async for water in water_collection.find():
#         try: 
#             _ =water["name"]
#             water = water_helper(water)
#         except:
#             water = cubic_water_helper(water)

#         waters.append(water)
#     return waters

# # async def retrieve_cubic_waters():
# #     waters = []
# #     async for water in water_collection.find():
# #         try: 
# #             _ = water["name"]
# #         except:
# #             print(water)
# #             water = cubic_water_helper(water)
            
# #         waters.append(water)
# #     print(waters)
# #     print(">>> RETURN CUBIC WATERs")
# #     return waters

# # Add a new water into to the database
# async def add_water(water_data: dict) -> dict:
#     water = await water_collection.insert_one(water_data)
#     new_water = await water_collection.find_one({"_id": water.inserted_id})
#     return water_helper(new_water)

# async def add_cubic_water(water_data: dict) -> dict:
#     water = await water_collection.insert_one(water_data)
#     new_water = await water_collection.find_one({"_id": water.inserted_id})
#     return cubic_water_helper(new_water)


# # Retrieve a water data with a matching ID
# async def retrieve_water(id: str) -> dict:
#     water = await water_collection.find_one({"_id": ObjectId(id)})
#     if water:
#         return water_helper(water)


# # Update a water with a matching ID
# async def update_water(id: str, data: dict):
#     # Return false if an empty request body is sent.
#     if len(data) < 1:
#         return False
#     water = await water_collection.find_one({"_id": ObjectId(id)})
#     if water:
#         updated_water = await water_collection.update_one(
#             {"_id": ObjectId(id)}, {"$set": data}
#         )
#         if updated_water:
#             return True
#         return False


# # Delete a water from the database