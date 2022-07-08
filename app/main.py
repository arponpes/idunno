import random

from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates

import forms
from models import Card, Response
from repository import CardRepo

app = FastAPI()

templates = Jinja2Templates(directory="templates")
app.mount("/static", StaticFiles(directory="static"), name="static")


@app.get("/card/", response_class=HTMLResponse)
async def get_all(request: Request):
    _cardList = await CardRepo.retrieve()
    return templates.TemplateResponse("list_of_cards.html", {"request": request, "id": id, "card_list": _cardList})


@app.delete("/card/{id}")
async def delete(id: str):
    await CardRepo.delete(id)
    return Response(code=200, status="Ok", message="Success delete data").dict(exclude_none=True)


@app.get("/card/random/", response_class=HTMLResponse)
async def random_card(request: Request):
    _cardList = await CardRepo.retrieve()
    _card = random.choice(_cardList)
    return templates.TemplateResponse("item.html", {"request": request, "id": id, "card": _card})


@app.get("/card/create/")
async def create_cards(request: Request):
    return templates.TemplateResponse("create_card_form.html", {"request": request})


@app.post("/card/create/")
async def create_card(request: Request):
    form = forms.JobCreateForm(request)
    await form.load_data()

    if form.is_valid():
        card = Card(a_side=form.a_side, b_side=form.b_side)
        await CardRepo.insert(card)
        return Response(code=200, status="Ok", message="Success save data").dict(exclude_none=True)
    return templates.TemplateResponse("create_card_form.html", form.__dict__)
