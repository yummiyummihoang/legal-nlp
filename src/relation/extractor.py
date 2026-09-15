"""Trích xuất quan hệ (Sửa đổi, bổ sung, bãi bỏ, hướng dẫn, dẫn chiếu)."""
from typing import List
from ..schemas.document import LegalRelation


def extract_legal_relations(text: str) -> List[LegalRelation]:
    """Phát hiện các quan hệ pháp lý giữa các thực thể hoặc văn bản."""
    raise NotImplementedError
