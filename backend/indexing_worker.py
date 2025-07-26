# backend/indexing_worker.py
import os
import logging
from tqdm import tqdm
from backend.file_utils import extract_text_from_file, compute_sha256
from backend.embeddings import embed_text
from backend.qdrant_client import ensure_collection, upsert_document
from backend.settings import SNIPPET_LENGTH

logger = logging.getLogger(__name__)

def index_documents_in_folder(folder_path: str):
    logger.info(f"📂 Inizio indicizzazione della cartella: {folder_path}")
    ensure_collection()

    files = [f for f in os.listdir(folder_path) if os.path.isfile(os.path.join(folder_path, f))]
    indexed_count = 0

    for file_name in tqdm(files, desc="Indicizzazione documenti"):
        file_path = os.path.join(folder_path, file_name)
        logger.info(f"📄 Elaborazione: {file_name}")

        text = extract_text_from_file(file_path)
        if not text:
            logger.warning(f"Nessun testo estratto da {file_name}, salto.")
            continue

        file_hash = compute_sha256(file_path)
        doc_id = file_hash[:36]  # Qdrant accetta UUID, tronchiamo a 36

        # Genera embedding
        vector = embed_text(text)
        snippet = text[:SNIPPET_LENGTH]

        upsert_document(
            doc_id,
            vector,
            {
                "file_name": file_name,
                "content": text,
                "snippet": snippet
            }
        )

        logger.info(f"✅ {file_name} indicizzato con successo.")
        indexed_count += 1

    logger.info(f"🏁 Indicizzazione completata. Totale documenti indicizzati: {indexed_count}")
