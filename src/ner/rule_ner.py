"""Trích xuất thực thể bằng rule/regex: Số hiệu văn bản, ngày tháng, điều khoản viện dẫn."""
from typing import List
from ..schemas.document import LegalEntity


def extract_entities_by_rules(text: str) -> List[LegalEntity]:
    """Trích xuất các thực thể chuẩn tắc qua biểu thức chính quy."""
    raise NotImplementedError
