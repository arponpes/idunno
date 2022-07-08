from models import Card
from database import db
import uuid


class CardRepo:
    @staticmethod
    async def retrieve():
        _card = []
        collection = db.get_collection("card").find()
        async for card in collection:
            _card.append(card)
        return _card

    @staticmethod
    async def insert(card: Card):
        id = str(uuid.uuid4())
        _card = {
            "_id": id,
            "a_side": card.a_side,
            "b_side": card.b_side,
        }
        await db.get_collection("card").insert_one(_card)

    @staticmethod
    async def update(id: str, card: Card):
        _card = await db.get_collection("card").find_one({"_id": id})
        _card["spanish"] = card.spanish
        _card["chinese"] = card.chinese
        _card["pinyin"] = card.pinyin
        await db.get_collection("card").update_one({"_id": id}, {"$set": _card})

    @staticmethod
    async def retrieve_id(id: str):
        return await db.get_collection("card").find_one({"_id": id})

    @staticmethod
    async def delete(id: str):
        await db.get_collection("card").delete_one({"_id": id})
