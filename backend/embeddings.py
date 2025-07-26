# backend/embeddings.py
from sentence_transformers import SentenceTransformer

from backend.settings import EMBEDDING_MODEL

# Carica modello una sola volta
model = SentenceTransformer(EMBEDDING_MODEL)

def embed_text(text: str):
    return model.encode([text], convert_to_numpy=True)[0]
