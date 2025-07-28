import os
from main import extract_outline

INPUT_DIR = "./input"
OUTPUT_DIR = "./output"

for filename in os.listdir(INPUT_DIR):
    if filename.lower().endswith(".pdf"):
        pdf_path = os.path.join(INPUT_DIR, filename)
        out_filename = os.path.splitext(filename)[0] + ".json"
        out_path = os.path.join(OUTPUT_DIR, out_filename)
        print(f"[📄] Processing {filename}")
        extract_outline(pdf_path, out_path)
