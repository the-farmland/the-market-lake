from fastapi import APIRouter, HTTPException
from pathlib import Path
import json

router = APIRouter()

@router.get("/product/{id}")
async def get_article(id: int):
    news_file = Path("data/products.json")
    if news_file.exists():
        with open(news_file, "r") as file:
            news_data = json.load(file)
        if 0 <= id < len(news_data):
            return {"article": news_data[id]}
        else:
            raise HTTPException(status_code=404, detail="Article not found")
    else:
        raise HTTPException(status_code=404, detail="News file not found")
