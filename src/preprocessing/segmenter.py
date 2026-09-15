"""Phân đoạn câu, đoạn văn bản pháp lý."""
from typing import List


def segment_sentences(text: str) -> List[str]:
    """Tách câu bảo toàn các số điều/khoản/ngày tháng."""
    return [s.strip() for s in text.splitlines() if s.strip()]
