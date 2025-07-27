from fastapi import FastAPI, UploadFile, File, HTTPException
from typing import Any, Optional, List, Dict
from pydantic import BaseModel
import logging
from .qdrant_client import QdrantClient
from .embeddings import EmbeddingModel
from .file_utils import process_uploaded_file

# Configurazione logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger(__name__)

app = FastAPI(
    title="Ricerca Semantica API",
    description="API per la ricerca semantica e gestione documenti",
    version="0.1.0"
)

# Inizializzazione servizi con gestione errori
try:
    qdrant = QdrantClient()
    model = EmbeddingModel()
except Exception as e:
    logger.critical(f"Failed to initialize services: {str(e)}")
    raise

# Modelli Pydantic
class SearchRequest(BaseModel):
    query: str
    filters: Optional[Dict[str, Any]] = None
    limit: int = 10

class UploadResponse(BaseModel):
    status: str
    document_id: str
    metadata: Dict[str, Any]

# Gestione errori centralizzata
async def handle_errors(coroutine):
    try:
        return await coroutine
    except ValueError as e:
        logger.error(f"Validation error: {str(e)}")
        raise HTTPException(status_code=400, detail=str(e))
    except Exception as e:
        logger.error(f"Unexpected error: {str(e)}")
        raise HTTPException(status_code=500)

# Endpoints
@app.post("/upload", response_model=UploadResponse)
async def upload_file(file: UploadFile = File(...)) -> UploadResponse:
    """
    Carica e processa un documento per l'indicizzazione semantica
    """
    contents = await file.read()
    try:
        result = process_uploaded_file(contents)
        return UploadResponse(
            status="success",
            document_id=result["document_id"],
            metadata=result["metadata"]
        )
    except Exception as e:
        await handle_errors(raise e)

@app.post("/search", response_model=List[Dict[str, Any]])
async def search(request: SearchRequest) -> List[Dict[str, Any]]:
    """
    Esegue una ricerca semantica con filtri opzionali
    """
    return await handle_errors(
        qdrant.search(
            query=request.query,
            filters=request.filters,
            limit=request.limit
        )
    )

@app.get("/health")
async def health_check() -> Dict[str, str]:
    """
    Endpoint di health check
    """
    return {"status": "healthy"}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)