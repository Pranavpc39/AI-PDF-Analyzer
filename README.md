# PDF Text Analyzer

A FastAPI application that answers questions about a PDF using retrieval-augmented generation (RAG). It extracts and chunks PDF text, stores embeddings in Qdrant, retrieves relevant passages for each question, and uses OpenAI to generate an answer.

## How it works

1. `app/index.py` loads `app/data/sample.pdf` and splits its text into overlapping chunks.
2. OpenAI creates embeddings for the chunks.
3. The chunks and embeddings are stored in a Qdrant collection named `sample_collection`.
4. The `/query/` endpoint searches Qdrant for relevant chunks and asks an OpenAI model to answer using the retrieved context.

## Requirements

- Python 3.10 or newer
- Docker with Docker Compose
- An OpenAI API key

## Setup

### 1. Clone the repository

```bash
git clone https://github.com/YOUR_USERNAME/YOUR_REPOSITORY.git
cd YOUR_REPOSITORY