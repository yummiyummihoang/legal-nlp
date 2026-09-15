# Legal NLP Pipeline

Hệ thống xử lý ngôn ngữ tự nhiên cho văn bản quy phạm pháp luật Việt Nam (Đầu ra trích xuất dạng file JSON chuẩn hóa).

## Cấu trúc thư mục

```
legal-nlp/
├── data/
│   ├── raw/                 # PDF/DOCX gốc, KHÔNG BAO GIỜ sửa
│   ├── interim/             # text đã extract, chưa clean
│   ├── processed/           # text đã normalize (đầu vào của pipeline)
│   ├── output/              # file JSON kết quả trích xuất cấu trúc văn bản
│   ├── annotations/         # file annotation (JSONL)
│   └── splits/              # train.txt / dev.txt / test.txt chứa doc_id
├── src/
│   ├── schemas/             # Pydantic models — nguồn sự thật duy nhất & JSON serializer
│   ├── ingestion/           # pdf_reader.py, docx_reader.py, ocr.py
│   ├── preprocessing/       # cleaner.py, normalizer.py, segmenter.py
│   ├── structure/           # rule_parser.py, classifier.py
│   ├── ner/                 # rule_ner.py, model_ner.py
│   ├── relation/            # extractor.py, resolver.py
│   ├── hierarchy/           # builder.py (stack-based hierarchy builder)
│   ├── evaluation/          # metrics.py, error_analysis.py
│   └── api/                 # FastAPI
├── notebooks/               # chỉ dùng để khám phá, không để code production
├── tests/                   # pytest — bắt buộc cho parser & hierarchy
├── configs/                 # YAML cấu hình model/đường dẫn
└── reports/                 # bảng kết quả, biểu đồ, error analysis
```

## Hướng dẫn cài đặt & sử dụng

```bash
# 1. Tạo môi trường ảo & cài đặt thư viện
python -m venv venv
venv\Scripts\activate  # Trên Windows
pip install -r requirements.txt

# 2. Chạy test
pytest tests/

# 3. Xuất kết quả ra file JSON
# Dùng LegalDocument.save_to_json(output_path="data/output/doc_id.json")
```
