# backend/api.py
from fastapi import APIRouter
from pydantic import BaseModel
import logging
from backend.indexing_worker import index_documents_in_folder
from backend.embeddings import embed_text
from backend.qdrant_client import search

logger = logging.getLogger(__name__)
router = APIRouter()

class IndexRequest(BaseModel):
    folder_path: str

class SearchRequest(BaseModel):
    query: str
    top_k: int = 5

@router.post("/index-folder")
def index_folder(req: IndexRequest):
    logger.info(f"📁 Richiesta indicizzazione cartella: {req.folder_path}")
    index_documents_in_folder(req.folder_path)
    return {"status": "ok", "message": "Indicizzazione completata."}

@router.post("/search")
def search_documents(req: SearchRequest):
    logger.info(f"🔎 Ricerca semantica per: '{req.query}'")
    query_vector = embed_text(req.query)
    results = search(query_vector, req.top_k)

    response = []
    for r in results:
        payload = r.payload
        response.append({
            "file_name": payload.get("file_name"),
            "score": round(r.score, 4),
            "snippet": payload.get("snippet", "")[:500],
            "file_url": f"/download/{payload.get('file_name')}"
        })

    return {"status": "ok", "results": response}
