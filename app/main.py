from fastapi import FastAPI
from repository import CardRepo
from models import Card, Response

app = FastAPI()


@app.get("/card/")
async def get_all():
    _cardList = await CardRepo.retrieve()
    return Response(code=200, status="Ok", message="Success retrieve all data", result=_cardList).dict(
        exclude_none=True
    )


@app.post("/card/create")
async def create(card: Card):
    await CardRepo.insert(card)
    return Response(code=200, status="Ok", message="Success save data").dict(exclude_none=True)


@app.get("/card/{id}")
async def get_id(id: str):
    _card = await CardRepo.retrieve_id(id)
    return Response(code=200, status="Ok", message="Success retrieve data", result=_card).dict(exclude_none=True)


@app.post("/card/update")
async def update(card: Card):
    await CardRepo.update(card.id, card)
    return Response(code=200, status="Ok", message="Success update data").dict(exclude_none=True)


@app.delete("/card/{id}")
async def delete(id: str):
    await CardRepo.delete(id)
    return Response(code=200, status="Ok", message="Success delete data").dict(exclude_none=True)
