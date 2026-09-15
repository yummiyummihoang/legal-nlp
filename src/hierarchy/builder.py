"""Xây dựng cấu trúc cây (Stack-based Hierarchy Builder): Văn bản -> Chương -> Điều -> Khoản -> Điểm."""
from typing import List
from ..schemas.document import LegalSection, HierarchyNode


class HierarchyBuilder:
    """Stack-based tree builder biến danh sách flat LegalSection thành cây phả hệ hoàn chỉnh."""

    def __init__(self):
        self.stack = []

    def build_tree(self, sections: List[LegalSection]) -> HierarchyNode:
        """Xây dựng cấu trúc phân cấp dùng thuật toán Stack."""
        raise NotImplementedError
