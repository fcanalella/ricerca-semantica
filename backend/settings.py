# backend/settings.py

COLLECTION_NAME = "semantic_rag"
QDRANT_HOST = "qdrant"
QDRANT_PORT = 6333

# Modello embeddings
EMBEDDING_MODEL = "sentence-transformers/paraphrase-multilingual-mpnet-base-v2"

# Numero massimo caratteri snippet
SNIPPET_LENGTH = 500
