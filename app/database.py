import os

import motor.motor_asyncio

MONGODB_URL = os.environ.get("MONGODB_URL")


client = motor.motor_asyncio.AsyncIOMotorClient(MONGODB_URL)

# connect to database python_db
db = client.python_db
