# tests/test_integration.py
# Minimal integration test: jalankan pipeline pada sample file (masukkan sample kecil di folder tests/data/)
import os
from main import run_local

def test_sample_docx():
    sample = "tests/data/input.pdf"
    if os.path.exists(sample):
        run_local([sample])
    else:
        print("No input.pdf found; place a sample in tests/data/input.pdf to run this test.")

if __name__ == '_main_':
    test_sample_docx()
