import json
import sys
from layout_parser import extract_text_blocks
from heading_ranker import score_heading_candidate
from utils import classify_heading_level, cluster_font_sizes

def extract_outline(pdf_path, json_out_path="output.json"):
    blocks = extract_text_blocks(pdf_path)
    font_sizes = [b["font_size"] for b in blocks]
    size_level_map = cluster_font_sizes(font_sizes)
    avg_font_size = sum(font_sizes) / len(font_sizes) if font_sizes else 12

    # Extract title
    title_candidates = [b for b in blocks if b['page'] == 1 and b['y'] < 200]
    title_candidates = sorted(title_candidates, key=lambda b: (-b['font_size'], b['y']))

    title_block = {"text": "Unknown"}
    if title_candidates:
        if len(title_candidates) >= 2 and abs(title_candidates[0]['y'] - title_candidates[1]['y']) < 30:
            title_block = {
                "text": title_candidates[0]["text"] + " " + title_candidates[1]["text"],
                "font_size": title_candidates[0]["font_size"],
                "is_bold": title_candidates[0]["is_bold"],
                "page": 1
            }
        else:
            title_block = title_candidates[0]

    # Extract headings
    outline = []
    for b in blocks:
        if b == title_block:
            continue
        b['score'] = score_heading_candidate(b, avg_font_size)
        level = classify_heading_level(b['font_size'], size_level_map)
        if level:
            outline.append({
                "level": level,
                "text": b['text'],
                "page": b['page']
            })

    result = {
        "title": title_block['text'],
        "outline": outline
    }

    with open(json_out_path, "w", encoding="utf-8") as f:
        json.dump(result, f, indent=4, ensure_ascii=False)

    print(f"[✅] Saved structured outline to {json_out_path}")

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python main.py <input.pdf> [output.json]")
        sys.exit(1)
    pdf_path = sys.argv[1]
    out_path = sys.argv[2] if len(sys.argv) > 2 else "output.json"
    extract_outline(pdf_path, out_path)