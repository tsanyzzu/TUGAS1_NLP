# tests/test_integration.py
# Minimal integration test: jalankan pipeline pada sample file (masukkan sample kecil di folder tests/data/)
import os
from main import run_local

def test_sample_docx():
    sample = "tests/data/sample.docx"
    if os.path.exists(sample):
        run_local([sample])
    else:
        print("No sample.docx found; place a sample in tests/data/sample.docx to run this test.")

if _name_ == '_main_':
    test_sample_docx()
