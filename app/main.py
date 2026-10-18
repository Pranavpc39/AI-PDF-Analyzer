from fastapi import FastAPI
from routes.query import router as query_router

app = FastAPI(
    title="RAG PDF Analyzer",
    description="This is the RAG API project to analyze the PDF",
    version="1.0.0"
)

app.include_router(query_router)