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

# Автоматически создаем папку images, если её нет
IMAGES_DIR.mkdir(parents=True, exist_ok=True)

app = FastAPI()

# Подключаем папку с картинками
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
    {"id": 9, "name": "Джоггеры Fleece", "category": "Штаны и Брюки", "price": 239000, "sizes": ["S", "M", "L", "XL"], "color": "#444b57", "image": "/images/30.png", "description": "Мягкий флис."},
    {"id": 10, "name": "Кепка Logo", "category": "Аксессуары", "price": 89000, "sizes": ["One"], "color": "#9a6b00", "image": "/images/31.png", "description": "Кепка."},
    {"id": 11, "name": "Куртка Windbreaker", "category": "Куртки и Ветровки", "price": 489000, "sizes": ["M", "L", "XL"], "color": "#b4234a", "image": "/images/32.png", "description": "Ветровка."},
    {"id": 12, "name": "Пуховик Short", "category": "Куртки и Ветровки", "price": 699000, "sizes": ["S", "M", "L"], "color": "#1d3557", "image": "/images/33.png", "description": "Пуховик."},
    {"id": 13, "name": "Очки Sunglasses", "category": "Аксессуары", "price": 189000, "sizes": ["One"], "color": "#22223b", "image": "/images/34.png", "description": "Очки."},
    {"id": 14, "name": "Очки Aviator", "category": "Аксессуары", "price": 219000, "sizes": ["One"], "color": "#7f5539", "image": "/images/35.png", "description": "Очки-авиаторы."},
    {"id": 15, "name": "Носки (3 пары)", "category": "Аксессуары", "price": 49000, "sizes": ["36-39", "40-43", "44-47"], "color": "#4a4e69", "image": "/images/36.png", "description": "Носки."},
    {"id": 17, "name": "Ремень Classic", "category": "Аксессуары", "price": 159000, "sizes": ["S", "M", "L"], "color": "#3e2723", "image": "/images/37.png", "description": "Ремень."},
    {"id": 18, "name": "Сумка Tote", "category": "Аксессуары", "price": 249000, "sizes": ["One"], "color": "#a68a64", "image": "/images/38.png", "description": "Сумка."},
    {"id": 19, "name": "Вязаное поло Striped", "category": "Худи и Свитшоты", "price": 389000, "sizes": ["M", "L", "XL"], "color": "#2b2b2b", "image": "/images/39.png", "description": "Вязаное поло."},
    {"id": 20, "name": "Свитшот Textured", "category": "Худи и Свитшоты", "price": 289000, "sizes": ["M", "L", "XL"], "color": "#e0e0e0", "image": "/images/40.png", "description": "Рельефная текстура."},
    {"id": 21, "name": "Джинсы Black Denim", "category": "Джинсы", "price": 349000, "sizes": ["30", "32", "34", "36"], "color": "#1a1a1a", "image": "/images/41.png", "description": "Черные джинсы."},
    {"id": 22, "name": "Бомбер Corduroy", "category": "Куртки и Ветровки", "price": 459000, "sizes": ["M", "L", "XL"], "color": "#5c4033", "image": "/images/42.png", "description": "Бомбер из вельвета."},
    {"id": 23, "name": "Бомбер Patched", "category": "Куртки и Ветровки", "price": 479000, "sizes": ["M", "L", "XL"], "color": "#121212", "image": "/images/43.png", "description": "Бомбер с нашивками."},
    {"id": 24, "name": "Пуховик Winter", "category": "Куртки и Ветровки", "price": 599000, "sizes": ["M", "L", "XL"], "color": "#2d2d2d", "image": "/images/44.png", "description": "Теплый пуховик."},
    {"id": 25, "name": "Шарф Plaid", "category": "Аксессуары", "price": 129000, "sizes": ["One"], "color": "#8b7d6b", "image": "/images/45.png", "description": "Шарф."},
    {"id": 26, "name": "Свитшот LITE", "category": "Худи и Свитшоты", "price": 319000, "sizes": ["M", "L", "XL"], "color": "#d2b48c", "image": "/images/46.png", "description": "Винтажный стиль."},
    {"id": 27, "name": "Кроссовки Chunky", "category": "Обувь", "price": 389000, "sizes": ["40", "41", "42", "43", "44"], "color": "#444", "image": "/images/47.png", "description": "Массивные кроссовки."},
    {"id": 28, "name": "Кардиган Knit", "category": "Худи и Свитшоты", "price": 369000, "sizes": ["M", "L", "XL"], "color": "#e3d5c8", "image": "/images/48.png", "description": "Вязаный кардиган."},
    {"id": 29, "name": "Худи Knit Black", "category": "Худи и Свитшоты", "price": 349000, "sizes": ["M", "L", "XL"], "color": "#121212", "image": "/images/49.png", "description": "Черное вязаное худи."},
    {"id": 30, "name": "Штаны Parachute", "category": "Штаны и Брюки", "price": 299000, "sizes": ["M", "L", "XL"], "color": "#2b2b2b", "image": "/images/50.png", "description": "Штаны-парашюты."},
]

class OrderItem(BaseModel):
    id: int
    z: str
    q: int

class Order(BaseModel):
    name: str
    phone: str
    items: List[OrderItem]
    account: str = ""

@app.get("/api/products")
def get_products():
    return PRODUCTS

@app.get("/api/products/{product_id}")
def get_product(product_id: int):
    for p in PRODUCTS:
        if p["id"] == product_id:
            return p
    raise HTTPException(status_code=404, detail="Товар не найден")

@app.get("/api/categories")
def get_categories():
    return ["Все", "Футболки и Лонгсливы", "Худи и Свитшоты", "Джинсы", "Штаны и Брюки", "Куртки и Ветровки", "Обувь", "Аксессуары"]

@app.post("/api/order")
def create_order(order: Order):
    text = f"🛍 **НОВЫЙ ЗАКАЗ В VELORI SHOP!**\n\n👤 **Имя:** {order.name}\n📞 **Телефон:** {order.phone}\n"
    if order.account:
        text += f"✈️ **Telegram:** {order.account}\n"
    text += f"\n📦 **Товары:**\n"
    
    total_price = 0
    first_image_rel_path = None

    for item in order.items:
        product = next((p for p in PRODUCTS if p["id"] == item.id), None)
        if product:
            item_total = product["price"] * item.q
            total_price += item_total
            text += f"• {product['name']} (Размер: {item.z}) — {item.q} шт. = {item_total:,} сум\n".replace(",", " ")
            if not first_image_rel_path:
                first_image_rel_path = product["image"].lstrip("/")
    
    text += f"\n💰 **ИТОГО:** {total_price:,} сум\n".replace(",", " ")
    
    image_file = (BASE / first_image_rel_path) if first_image_rel_path else None

    try:
        # Если папка images на сервере есть и файл картинки на месте — отправляем с фото
        if image_file and image_file.is_file():
            url = f"https://api.telegram.org/bot{TELEGRAM_BOT_TOKEN}/sendPhoto"
            with open(image_file, "rb") as photo:
                payload = {"chat_id": TELEGRAM_CHAT_ID, "caption": text, "parse_mode": "Markdown"}
                response = requests.post(url, data=payload, files={"photo": photo})
        else:
            # Иначе отправляем текстом, чтобы заказ всё равно дошел до вас
            url = f"https://api.telegram.org/bot{TELEGRAM_BOT_TOKEN}/sendMessage"
            payload = {"chat_id": TELEGRAM_CHAT_ID, "text": text, "parse_mode": "Markdown"}
            response = requests.post(url, json=payload)

        response.raise_for_status()
        return {"ok": True, "id": f"TG-{randint(1000, 9999)}"}
    except Exception as e:
        print(f"Ошибка отправки в Telegram: {e}")
        return {"ok": False, "error": "Не удалось отправить заказ"}
