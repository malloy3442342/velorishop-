from pathlib import Path
from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import FileResponse
from fastapi.staticfiles import StaticFiles
from pydantic import BaseModel
from typing import List
import requests
from random import randint

BASE = Path(__file__).parent
IMAGES_DIR = BASE / "images"

# Автоматически создаем папку images, если ее еще нет
IMAGES_DIR.mkdir(parents=True, exist_ok=True)

app = FastAPI()

# Подключаем статическую папку для изображений
app.mount("/images", StaticFiles(directory=str(IMAGES_DIR)), name="images")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"], 
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
def read_index():
    return FileResponse(BASE / "index.html")

TELEGRAM_BOT_TOKEN = "8887560505:AAGxgDxNzgngS6ZHjmO3gL9FCn1Nzo1W1Vs"
TELEGRAM_CHAT_ID = "8800476098"

class Product(BaseModel):
    id: int
    name: str
    category: str
    price: int
    sizes: List[str]
    color: str
    image: str
    description: str

PRODUCTS = [
    {"id": 1, "name": "Футболка Basic", "category": "Футболки и Лонгсливы", "price": 129000, "sizes": ["S", "M", "L", "XL"], "color": "#2f5bff", "image": "/images/22.png", "description": "Плотный хлопок 100%."},
    {"id": 2, "name": "Футболка Oversize", "category": "Футболки и Лонгсливы", "price": 159000, "sizes": ["M", "L", "XL"], "color": "#1f7a5c", "image": "/images/23.png", "description": "Свободный крой."},
    {"id": 3, "name": "Футболка Print", "category": "Футболки и Лонгсливы", "price": 149000, "sizes": ["S", "M", "L"], "color": "#c2410c", "image": "/images/24.png", "description": "Яркий принт."},
    {"id": 4, "name": "Худи Heavy", "category": "Худи и Свитшоты", "price": 329000, "sizes": ["S", "M", "L", "XL"], "color": "#8a3ffc", "image": "/images/25.png", "description": "Флис 400г."},
    {"id": 5, "name": "Худи на молнии", "category": "Худи и Свитшоты", "price": 359000, "sizes": ["M", "L", "XL"], "color": "#c2410c", "image": "/images/26.png", "description": "Удобная молния."},
    {"id": 6, "name": "Свитшот Crew", "category": "Худи и Свитшоты", "price": 279000, "sizes": ["S", "M", "L"], "color": "#0f766e", "image": "/images/27.png", "description": "Классический вырез."},
    {"id": 7, "name": "Джинсы Straight", "category": "Джинсы", "price": 319000, "sizes": ["30", "32", "34", "36"], "color": "#334e7a", "image": "/images/28.png", "description": "Прямой крой."},
    {"id": 8, "name": "Карго Utility", "category": "Штаны и Брюки", "price": 349000, "sizes": ["30", "32", "34"], "color": "#5b6b3a", "image": "/images/29.png", "description": "Множество карманов."},
    {"id": 9, "name": "Джоггеры Fleece", "category": "Штаны и Брюки", "price": 239000, "sizes": ["S", "M", "L", "XL"], "color": "#444b57", "image": "/images/30.png", "description": "Мягкий ф