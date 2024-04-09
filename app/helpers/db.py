"""Mongodb instance """
import os
from motor.motor_asyncio import AsyncIOMotorClient


class DataBase:
    """DataBase class"""
    client: AsyncIOMotorClient = None


db = DataBase()


async def get_db() -> AsyncIOMotorClient:
    """get db instance"""
    db.client = AsyncIOMotorClient(os.getenv("MONGODB_URL"))
    return db.client.get_database()
