import random

from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates

from models import Card, Response
from repository import CardRepo

app = FastAPI()

templates = Jinja2Templates(directory="templates")
app.mount("/static", StaticFiles(directory="static"), name="static")


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


@app.get("/card/{id}", response_class=HTMLResponse)
async def get_id(request: Request, id: str):
    _card = await CardRepo.retrieve_id(id)
    return templates.TemplateResponse("item.html", {"request": request, "id": id, "card": _card})


@app.post("/card/update")
async def update(card: Card):
    await CardRepo.update(card.id, card)
    return Response(code=200, status="Ok", message="Success update data").dict(exclude_none=True)


@app.delete("/card/{id}")
async def delete(id: str):
    await CardRepo.delete(id)
    return Response(code=200, status="Ok", message="Success delete data").dict(exclude_none=True)


@app.get("/card/random/", response_class=HTMLResponse)
async def random_card(request: Request):
    _cardList = await CardRepo.retrieve()
    _card = random.choice(_cardList)
    return templates.TemplateResponse("item.html", {"request": request, "id": id, "card": _card})
