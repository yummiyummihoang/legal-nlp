"""Phân tích cấu trúc theo luật/regex: Phần, Chương, Mục, Điều, Khoản, Điểm."""
from typing import List
from ..schemas.document import LegalSection


def parse_legal_structure_rules(text: str) -> List[LegalSection]:
    """Phân rã văn bản thành danh sách các LegalSection."""
    raise NotImplementedError
