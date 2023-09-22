from pprint import pprint
from typing import Dict

from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates

app = FastAPI()
templates = Jinja2Templates(directory="templates")


@app.post('/dataset/snapshot')
async def snapshots(d: Dict):
    data = {
        "name": d['name'],
        "age": d['age']
    }
    return {"data": data}


@app.get("/", response_class=HTMLResponse)
async def read_root(request: Request):
    name = "Post dataset"
    title = "test"
    return templates.TemplateResponse("index.html", {"request": request, 'title': title, 'name': name})
