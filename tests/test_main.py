import random

from app.main import app
from fastapi.testclient import TestClient

client = TestClient(app)


CARDS = [
    {"chinese": "一", "id": "1", "pinyin": "yī", "spanish": "uno"},
    {"chinese": "二", "id": "2", "pinyin": "èr", "spanish": "dos"},
    {"chinese": "三", "id": "3", "pinyin": "sān", "spanish": "tres"},
    {"chinese": "四", "id": "4", "pinyin": "sì", "spanish": "cuatro"},
    {"chinese": "五", "id": "5", "pinyin": "wǔ", "spanish": "cinco"},
]


def test_get_random_card():
    random_method = random.choice
    random.choice = lambda x: CARDS[0]
    response = client.get("/card/1")
    random.choice = random_method
    assert response.status_code == 200
    assert response.json() == CARDS[0]


def test_assert_randomness():
    cards = set()
    for _ in range(10):
        response = client.get("/card/")
        cards.add(response.json()["id"])
    assert len(cards) > 1


def test_post_card():
    response = client.post("/card/")
    assert response.status_code == 405
