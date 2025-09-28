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
- Dual-mode: dapat dijalankan di Google Colab (upload file) atau di lingkungan lokal lewat argumen CLI.

---

## Struktur proyek
