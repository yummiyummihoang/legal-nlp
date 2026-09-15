"""FastAPI server cung cấp API trích xuất cấu trúc văn bản pháp lý."""
from fastapi import FastAPI
from ..schemas.document import LegalDocument

app = FastAPI(title="Legal NLP Service", version="1.0.0")


@app.get("/")
def health_check():
    return {"status": "ok", "service": "legal-nlp"}


@app.post("/parse", response_model=LegalDocument)
def parse_document(raw_text: str):
    """Endpoint phân tích văn bản pháp lý."""
    raise NotImplementedError
