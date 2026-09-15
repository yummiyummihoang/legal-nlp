"""Pydantic models - Nguồn sự thật duy nhất cho toàn bộ pipeline."""
from typing import List, Optional, Dict, Any
from pydantic import BaseModel, Field


class LegalEntity(BaseModel):
    id: str = Field(..., description="Định danh thực thể")
    text: str = Field(..., description="Văn bản thực thể")
    label: str = Field(..., description="Loại thực thể (VD: LAW_REF, DATE, ORG, SIGNER)")
    start_char: int = Field(..., description="Vị trí bắt đầu trong text gốc")
    end_char: int = Field(..., description="Vị trí kết thúc trong text gốc")
    metadata: Dict[str, Any] = Field(default_factory=dict)


class LegalRelation(BaseModel):
    source_id: str = Field(..., description="ID thực thể nguồn")
    target_id: str = Field(..., description="ID thực thể đích")
    relation_type: str = Field(..., description="Loại quan hệ (VD: AMENDS, REPLACES, REFERENCES)")
    metadata: Dict[str, Any] = Field(default_factory=dict)


class LegalSection(BaseModel):
    section_id: str = Field(..., description="Mã mục (VD: Chuong_I, Dieu_1, Khoan_2, Diem_a)")
    section_type: str = Field(..., description="Loại (VD: PHAN, CHUONG, MUC, DIEU, KHOAN, DIEM)")
    title: Optional[str] = Field(None, description="Tiêu đề của mục")
    content: str = Field(..., description="Nội dung văn bản của mục")
    entities: List[LegalEntity] = Field(default_factory=list)


class HierarchyNode(BaseModel):
    node_id: str
    level: str  # doc, part, chapter, section, article, clause, point
    title: Optional[str] = None
    content: Optional[str] = None
    children: List["HierarchyNode"] = Field(default_factory=list)


HierarchyNode.update_forward_refs()


class LegalDocument(BaseModel):
    doc_id: str = Field(..., description="Định danh duy nhất của văn bản")
    doc_number: Optional[str] = Field(None, description="Số/ký hiệu văn bản")
    title: Optional[str] = Field(None, description="Trích yếu / tiêu đề văn bản")
    doc_type: Optional[str] = Field(None, description="Loại văn bản: Luat, Nghi_dinh, Thong_tu...")
    issuer: Optional[str] = Field(None, description="Cơ quan ban hành")
    issued_date: Optional[str] = Field(None, description="Ngày ban hành")
    effective_date: Optional[str] = Field(None, description="Ngày có hiệu lực")
    sections: List[LegalSection] = Field(default_factory=list)
    relations: List[LegalRelation] = Field(default_factory=list)
    hierarchy: Optional[HierarchyNode] = None
    raw_text: Optional[str] = None
    metadata: Dict[str, Any] = Field(default_factory=dict)

    def save_to_json(self, output_path: str, indent: int = 2) -> None:
        """Xuất thông tin văn bản ra file JSON với bảng mã UTF-8."""
        from pathlib import Path
        p = Path(output_path)
        p.parent.mkdir(parents=True, exist_ok=True)
        with open(p, "w", encoding="utf-8") as f:
            # Pydantic v2 model_dump_json or v1 json fallback
            if hasattr(self, "model_dump_json"):
                f.write(self.model_dump_json(indent=indent))
            else:
                f.write(self.json(indent=indent, ensure_ascii=False))

    @classmethod
    def load_from_json(cls, json_path: str) -> "LegalDocument":
        """Đọc và parse một LegalDocument từ file JSON."""
        from pathlib import Path
        with open(Path(json_path), "r", encoding="utf-8") as f:
            content = f.read()
        if hasattr(cls, "model_validate_json"):
            return cls.model_validate_json(content)
        return cls.parse_raw(content)
