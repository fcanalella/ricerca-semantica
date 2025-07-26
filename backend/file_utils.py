# backend/file_utils.py
import os
import hashlib
import fitz  # PyMuPDF
import logging

logger = logging.getLogger(__name__)

def extract_text_from_file(file_path: str) -> str:
    logger.info(f"[extract_text_from_file] Analisi file: {file_path}")
    ext = os.path.splitext(file_path)[-1].lower()

    text = ""
    if ext == ".txt":
        with open(file_path, "r", encoding="utf-8", errors="ignore") as f:
            text = f.read()
        logger.info(f"[TXT] Estratti {len(text)} caratteri da: {file_path}")
    elif ext == ".pdf":
        doc = fitz.open(file_path)
        text = " ".join([page.get_text("text") for page in doc])
        doc.close()
        logger.info(f"[PDF] Estratti {len(text)} caratteri da: {file_path}")
    else:
        logger.warning(f"Formato non supportato: {ext}")

    return text.strip()

def compute_sha256(file_path: str) -> str:
    logger.info(f"[compute_sha256] Calcolo hash per: {file_path}")
    h = hashlib.sha256()
    with open(file_path, "rb") as f:
        for chunk in iter(lambda: f.read(4096), b""):
            h.update(chunk)
    hash_val = h.hexdigest()
    logger.info(f"[compute_sha256] Hash calcolato: {hash_val}")
    return hash_val
