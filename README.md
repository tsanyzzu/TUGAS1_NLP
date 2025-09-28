# PDF & DOCX → Structured Markdown / JSON Extractor

**Ringkasan singkat**  
Proyek ini mengimplementasikan pipeline ekstraksi teks dari file PDF (.pdf) dan Microsoft Word (.docx) dan mengubahnya menjadi struktur hierarki yang cocok untuk analisis NLP (format JSON dan Markdown). Implementasi ditujukan untuk tugas berkelompok (laporan/skripsi) dan mudah dijalankan di **Google Colab** atau **lokal** (CLI).

---

## Fitur
- Ekstraksi teks dari PDF (menggunakan `pdfplumber`).
- Ekstraksi paragraf dan pengecekan style dari DOCX (menggunakan `python-docx`).
- Heuristik deteksi heading (nomor bab, 1., 1.1, BAB I, baris ALL-CAPS) untuk membangun struktur hierarki.
- Ekspor hasil ke:
  - `*_structured.json` (tree JSON)
  - `*_structured.md` (Markdown yang terstruktur)

---

## Struktur proyek

pdf-docx-extractor/
├─ extractor/
│ ├─ init.py
│ ├─ pdf_extractor.py
│ ├─ docx_extractor.py
│ └─ hierarchy.py
├─ utils/
│ ├─ init.py
│ └─ io_helpers.py
├─ main.py # entry point - mendukung Colab & CLI
├─ run_local.py # contoh pemakaian CLI (opsional)
├─ requirements.txt
├─ README.md
└─ tests/
└─ test_integration.py

---

## Instalasi (lokal)
1. Buat virtualenv (opsional) dan aktifkan.
2. Install dependency:
```bash
pip install -r requirements.txt
