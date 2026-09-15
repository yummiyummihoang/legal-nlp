"""Trích xuất thực thể bằng Pretrained LM (PhoBERT, Legal-BERT...)."""
from typing import List
from ..schemas.document import LegalEntity


def extract_entities_by_model(text: str) -> List[LegalEntity]:
    """Trích xuất thực thể phức tạp bằng Deep Learning / LLM."""
    raise NotImplementedError
