# backend/qdrant_client.py
from qdrant_client import QdrantClient
from backend.settings import QDRANT_HOST, QDRANT_PORT, COLLECTION_NAME

qdrant = QdrantClient(host=QDRANT_HOST, port=QDRANT_PORT)

def ensure_collection():
    if COLLECTION_NAME not in [c.name for c in qdrant.get_collections().collections]:
        qdrant.create_collection(
            collection_name=COLLECTION_NAME,
            vectors_config={"size": 768, "distance": "Cosine"}  # 768 per mpnet
        )

def upsert_document(doc_id: str, vector, payload: dict):
    qdrant.upsert(
        collection_name=COLLECTION_NAME,
        points=[{
            "id": doc_id,
            "vector": vector,
            "payload": payload
        }]
    )

def search(query_vector, top_k: int = 5):
    return qdrant.search(
        collection_name=COLLECTION_NAME,
        query_vector=query_vector,
        limit=top_k
    )
