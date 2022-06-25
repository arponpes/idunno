import random

from app.main import CARDS, app
from fastapi.testclient import TestClient

client = TestClient(app)


def test_get_random_card():
    random_method = random.choice
    random.choice = lambda x: CARDS[0]
    response = client.get("/")
    random.choice = random_method
    assert response.status_code == 200
    assert response.json() == {"chinese": "一", "id": "1", "pinyin": "yī", "spanish": "uno"}


def test_assert_randomness():
    cards = set()
    for _ in range(10):
        response = client.get("/")
        cards.add(response.json()["id"])
    assert len(cards) > 1


def test_post_card():
    response = client.post("/")
    assert response.status_code == 405
