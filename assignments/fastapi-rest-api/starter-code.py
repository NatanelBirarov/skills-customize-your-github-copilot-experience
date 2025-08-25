from fastapi import FastAPI, Request
from typing import List, Dict
from fastapi.responses import JSONResponse

app = FastAPI()

# In-memory data store
items: List[Dict] = []

@app.get("/hello")
def hello():
    return {"message": "Hello, FastAPI!"}

@app.get("/info")
def info():
    return {"framework": "FastAPI", "purpose": "REST API demo"}

@app.post("/items")
def add_item(item: Dict):
    items.append(item)
    return {"status": "Item added", "item": item}

@app.get("/items")
def get_items():
    return {"items": items}

# To run: uvicorn starter-code:app --reload
