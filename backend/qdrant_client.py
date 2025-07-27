import os
from qdrant_client import QdrantClient
from typing import Optional, List, Dict, Any
import logging
from pydantic import BaseSettings

class QdrantConfig(BaseSettings):
    host: str = os.getenv("QDRANT_HOST", "localhost")
    port: int = os.getenv("QDRANT_PORT", 6333)

class QdrantClientWrapper:
    """
    Wrapper per il client Qdrant con gestione errori e logging.
    Configurazione tramite variabili d'ambiente:
    - QDRANT_HOST: indirizzo del server (default: localhost)
    - QDRANT_PORT: porta del server (default: 6333)
    """
    def __init__(self):
        config = QdrantConfig()
        self.client = QdrantClient(
            host=config.host, 
            port=config.port
        )
        self.logger = logging.getLogger(__name__)
        
    def upsert_document(self, 
                      collection: str, 
                      points: List[dict]) -> bool:
        """
        Inserisce documenti in Qdrant.
        Restituisce True se successo, False altrimenti.
        Logga gli errori senza sollevare eccezioni.
        """
        try:
            self.client.upsert(
                collection_name=collection,
                points=points
            )
            self.logger.info(f"Upsert successful in collection '{collection}'")
            return True
        except Exception as e:
            self.logger.error(f"Upsert failed in collection '{collection}': {str(e)}")
            return False

    def search(self, 
              collection: str, 
              query_vector: List[float], 
              limit: Optional[int] = 10) -> List[Dict[str, Any]]:
        """
        Esegue ricerche semantiche in Qdrant.
        Solleva eccezioni per gestione esterna.
        """
        try:
            results = self.client.search(
                collection_name=collection,
                query_vector=query_vector,
                limit=limit
            )
            self.logger.debug(f"Search found {len(results)} results")
            return results
        except Exception as e:
            self.logger.error(f"Search failed in collection '{collection}': {str(e)}")
            raise ValueError(f"Search error: {str(e)}") from e
