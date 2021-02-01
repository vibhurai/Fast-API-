from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
import requests
import json


app = FastAPI()


templates = Jinja2Templates(directory="templates")


@app.get("/", response_class=HTMLResponse)
async def read_item(request: Request):
    return templates.TemplateResponse("items.html" ,{"request": request})

@app.get("/image/{city}", response_class=HTMLResponse)
async def read_item(city :str, request: Request):
    response = requests.get(f'https://api.unsplash.com/search/photos?query={city}&client_id=LaAjTPCHjo94dIZJO7hqW50jBgfP64crCwv__xA-PBQ')
    ans = response.json()
    image_ = ans['results'][0]['urls']['regular']
    return templates.TemplateResponse("image.html" ,{"request": request, "image_url": image_})
    