# backend/main.py
from fastapi import FastAPI
from backend import api
import logging

logging.basicConfig(level=logging.INFO)

app = FastAPI(title="Semantic RAG API")
app.include_router(api.router)

@app.get("/")
def read_root():
    return {"message": "API Semantic RAG attiva"}
