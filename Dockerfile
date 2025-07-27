FROM python:3.9-slim

WORKDIR /app

# Variabili d'ambiente
ENV EMBEDDING_MODEL="paraphrase-multilingual-MiniLM-L12-v2"
ENV QDRANT_HOST="qdrant"
ENV PYTHONUNBUFFERED=1

# Installazione dipendenze
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copia codice
COPY . .

CMD ["uvicorn", "backend.main:app", "--host", "0.0.0.0"]
