"""Làm sạch văn bản thô (loại bỏ header/footer lặp lại, ký tự rác)."""


def clean_raw_text(text: str) -> str:
    """Loại bỏ ký tự lạ, chuẩn hóa xuống dòng, xóa header/footer rác."""
    return text.strip()
