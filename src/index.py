from fastapi import FastAPI
from fastapi.responses import HTMLResponse
from src.dtos.ISayHelloDto import ISayHelloDto
from src.routes.ArticleRoute import router as article_router
from src.controllers.departments.groceries.The_Groceries_Controller import router as groceries_router
import json
from pathlib import Path

app = FastAPI()

@app.get("/", response_class=HTMLResponse)
async def root():
    return """
    <div style="background-image: url('https://www.plus-us.com/home.jpg'); height: 100vh; display: flex; align-items: center; justify-content: center;">
    </div>
    """

@app.get("/hello/{name}")
async def say_hello(name: str):
    return {"message": f"Hello {name}"}

@app.post("/hello")
async def hello_message(dto: ISayHelloDto):
    return {"message": f"Hello {dto.message}"}

@app.get("/news")
async def get_news():
    news_file = Path("data/products.json")
    if news_file.exists():
        with open(news_file, "r") as file:
            news_data = json.load(file)
        return {"news": news_data}
    else:
        return {"message": "News file not found"}

# Include the article routes
app.include_router(article_router)

# Include the groceries routes
app.include_router(groceries_router)  # Groceries controller includes savings)
