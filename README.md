# Ricerca Semantica Avanzata

![Python 3.12](https://img.shields.io/badge/Python-3.12-blue)
![Qdrant](https://img.shields.io/badge/Vector_DB-Qdrant-green)
![Multilingual](https://img.shields.io/badge/Model-paraphrase--multilingual--mpnet--base--v2-orange)

Un sistema di ricerca ibrido che combina:
- **Ricerca semantica** (embedding multilingue)
- **Filtri strutturati** (protocollo, date, mittenti)
- **Gestione documentale avanzata** (PDF, DOC, EML con allegati, OCR)

## 🚀 Funzionalità Principali

- **Supporto documenti**:
  - 📄 PDF (con estrazione testo e OCR immagini)
  - 📝 Documenti Office (DOC, DOCX)
  - ✉ EML (con gestione allegati padre-figlio)
  - 📝 File di testo semplice

- **Ricerca ibrida**:
  - 🔍 Ricerca semantica full-text
  - ⚙ Filtri per metadati:
    - Protocollo
    - Intervallo date
    - Mittente/Destinatario
    - Tag personalizzati

- **Deployment**:
  - 🐳 Docker e Docker-compose
  - 📦 Modelli ML persistenti
  - 🗄 Database Qdrant con volume dedicato

## 🏗 Struttura del Progetto

```bash
🗂 STRUTTURA COMPLETA DEL PROGETTO (Con Python 3.12 e modello "paraphrase-multilingual-mpnet-base-v2")
bash
ricerca-semantica/
├── .docker/
│   ├── qdrant/
│   │   ├── docker-compose.yml          # Configurazione container Qdrant
│   │   └── qdrant-config.yml           # Configurazione performance
├── .github/
│   └── workflows/
│       ├── ci.yml                      # Continuous Integration
│       └── deploy.yml                  # Deployment
├── backend/
│   ├── src/
│   │   ├── core/
│   │   │   ├── document_processing/
│   │   │   │   ├── pdf_handler.py      # Gestione PDF + OCR
│   │   │   │   ├── eml_handler.py      # Parser EML + allegati
│   │   │   │   ├── office_handler.py   # Doc/Docx/Txt
│   │   │   │   └── ocr_engine.py       # Configurazione Tesseract
│   │   │   ├── models/
│   │   │   │   └── multilingual.py     # Wrapper per il modello
│   │   │   ├── database/
│   │   │   │   ├── qdrant_connector.py # Gestione connessione
│   │   │   │   └── file_tracker.db     # SQLite per file indicizzati
│   │   │   └── search/
│   │   │       ├── hybrid_engine.py    # Ricerca semantica + campi
│   │   │       └── query_builder.py    # Costruzione query
│   │   ├── api/
│   │   │   ├── endpoints/
│   │   │   │   ├── search.py           # Endpoint ricerca
│   │   │   │   └── upload.py           # Endpoint caricamento
│   │   │   └── fastapi_app.py          # Configurazione FastAPI
│   │   └── utils/
│   │       ├── logger.py               # Logging
│   │       └── config_manager.py       # Gestione configurazioni
│   ├── tests/
│   │   ├── unit/
│   │   └── integration/
│   ├── Dockerfile                      # Immagine Python 3.12
│   ├── requirements.txt                # Dipendenze con versioni
│   └── pyproject.toml                  # Configurazione progetto
├── frontend/
│   ├── public/
│   │   ├── assets/                     # Immagini/icone
│   │   └── favicon.ico
│   ├── src/
│   │   ├── components/
│   │   │   ├── Search/
│   │   │   │   ├── FiltersPanel.vue    # Filtri protocollo/data
│   │   │   │   └── ResultsList.vue     # Visualizzazione risultati
│   │   │   ├── Upload/
│   │   │   │   └── DragDropZone.vue    # Area caricamento
│   │   │   └── Document/
│   │   │       ├── TreeView.vue        # Vista gerarchica EML
│   │   │       └── OCRPreview.vue      # Testo estratto da immagini
│   │   ├── composables/
│   │   │   └── useSearch.js           # Logica ricerca
│   │   ├── stores/
│   │   │   └── searchStore.js         # Stato ricerca (Pinia)
│   │   ├── App.vue
│   │   └── main.js
│   ├── Dockerfile                      # Build Vue/React
│   └── package.json
├── data/
│   ├── models/
│   │   └── paraphrase-multilingual-mpnet-base-v2/  # Modello persistente
│   ├── knowledge/
│   │   ├── generali/                   # Documenti generici
│   │   │   ├── documento1.pdf
│   │   │   └── nota1.eml
│   │   ├── note_acquisite/             # Categoria 1
│   │   ├── note_trasmesse/             # Categoria 2
│   │   └── processed/                  # Testo estratto
│   │       ├── file_hashes.json        # Tracciamento modifiche
│   │       └── extracted/
│   │           ├── generali/
│   │           │   └── documento1.json # {testo, metadati, ocr_text}
│   ├── qdrant/                         # Volume database
│   └── tesseract/                      # Dati OCR
├── Makefile                            # Comandi principali
├── docker-compose.yml                  # Orchestrazione globale
└── README.md                           # Documentazione



🛠 Prerequisiti
Docker 20+

Docker-compose 2.4+

Python 3.12 (solo per sviluppo locale)

🚀 Installazione
Clona il repository:

bash
git clone https://github.com/fcanalella/ricerca-semantica.git
cd ricerca-semantica
Avvia i servizi:

bash
docker-compose -f .docker/qdrant/docker-compose.yml up -d
docker-compose up --build
Accedi all'interfaccia:

Frontend: http://localhost:3000

API Docs: http://localhost:8000/docs

🔧 Configurazione
Modificare i file:

.docker/qdrant/qdrant-config.yml → Regole performance Qdrant

backend/src/utils/config_manager.py → Parametri applicazione

🤖 Pipeline di Indicizzazione

Code
graph TD
    A[Caricamento file] --> B{Estrazione testo}
    B -->|PDF| C[OCR immagini]
    B -->|EML| D[Estrazione allegati]
    C --> E[Generazione embedding]
    D --> E
    E --> F[Salvataggio Qdrant]





📄 Licenza
MIT License - Copyright (c) 2023 Francesco Canalella

📬 Contatti
Per domande o supporto:

📧 Email: fcanalella@gmail.com

💬 Issue tracker GitHub

text

### 🔍 Versioni Componenti Principali
| Componente               | Versione |
|--------------------------|----------|
| Python                   | 3.12     |
| Qdrant                   | 1.7.x    |
| Sentence-Transformers    | 2.2.2    |
| Tesseract OCR            | 5.3      |
| FastAPI                  | 0.95+    |

**Note**: 
- Il README include badge dinamici per versioni
- Diagrammi Mermaid per visualizzare i flussi
- Tabelle di configurazione chiare
- Istruzioni di deployment complete

Vuoi aggiungere altre sezioni (es. screenshot, demo online, roadmap)?
si roadmap
Ecco la sezione Roadmap da aggiungere al tuo README.md (prima della licenza), con timeline realistica e milestone chiare:

markdown
## 🗺 Roadmap (2023-2024)

### **Q4 2023 - Core Funzionalità**
```mermaid
gantt
    title Fase 1 - Implementazione Base
    dateFormat  YYYY-MM-DD
    section Indicizzazione
    Parser File (PDF/DOC/EML)       :done,    des1, 2023-10-01, 15d
    OCR Integrazione                 :done,    des2, 2023-10-16, 10d
    Gestione Allegati EML            :done,    des3, 2023-10-20, 7d
    section Ricerca
    Hybrid Search Base               :done,    des4, 2023-11-01, 14d
    Filtri Metadati                  :done,    des5, 2023-11-15, 10d

Q1 2024 - Ottimizzazioni
Performance Scaling
Sharding Qdrant (cluster mode)
Cache Redis per ricerche frequenti
Advanced NLP
Reranker cross-encoder (↑ precisione)
Supporto lingue aggiuntive (cinese, arabo)
UI/UX
Export risultati (CSV/JSON)
Dark mode
Q2 2024 - Feature Avanzate
Controllo Accessi
Autenticazione JWT
ACL per documenti sensibili
Workflow Approvazione
Moderazione contenuti
Approvazione prima di indicizzazione
Integrazioni Cloud
S3-compatible storage
Backup automatizzato su AWS/GCP

📌 Metriche di Successo
KPI	Target 2024
Tempo indicizzazione	< 2s/doc
Precisione ricerca	> 92%
Supporto lingue	10+
Concurrent users	100+
text

### Perché questa roadmap?
1. **Focalizzazione su MVP**: Prima le funzionalità core (indicizzazione/ricerca)
2. **Evoluzione Graduale**: Dalla single-machine al cluster
3. **Priorità Business**: 
   - Prima le feature essenziali (OCR, filtri)
   - Poi sicurezza e governance (Q1 2024)
4. **Misurabilità**: KPI quantificabili per ogni fase
