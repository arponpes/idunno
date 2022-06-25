import random

from fastapi import FastAPI

app = FastAPI()

CARDS = [
    {"id": "1", "spanish": "uno", "chinese": "一", "pinyin": "yī"},
    {"id": "2", "spanish": "dos", "chinese": "二", "pinyin": "èr"},
    {"id": "3", "spanish": "tres", "chinese": "三", "pinyin": "sān"},
    {"id": "4", "spanish": "cuatro", "chinese": "四", "pinyin": "sì"},
]


@app.get("/")
async def get_card():
    return random.choice(CARDS)
