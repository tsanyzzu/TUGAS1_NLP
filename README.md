# PDF & DOCX → Structured Markdown / JSON Extractor

**Ringkasan singkat**  
Proyek ini mengimplementasikan pipeline ekstraksi teks dari file PDF (.pdf) dan Microsoft Word (.docx) dan mengubahnya menjadi struktur hierarki yang cocok untuk analisis NLP (format JSON dan Markdown).

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

```text
pdf-docx-extractor/
├─ extractor/
│  ├─ __init__.py
│  ├─ pdf_extractor.py
│  ├─ docx_extractor.py
│  └─ hierarchy.py
├─ utils/
│  ├─ __init__.py
│  └─ io_helpers.py
├─ main.py
├─ requirements.txt
├─ README.md
└─ tests/
   └─ test_integration.py
```

---

## Instalasi
1. Install dependency:
```bash
pip install -r requirements.txt
```

### Anggota Kelompok

1. Arif Athaya Harahap — 235150200111056
2. Ariiq Tsany Zu — 235150200111049
3. Fadhlullah Akmal — 235150207111068
4. Muhammad Rafly Ash Shiddiqi — 235150207111062
5. Rashky Rahmadian Jauhara — 235150201111066