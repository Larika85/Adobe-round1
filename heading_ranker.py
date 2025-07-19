import re
def multilingual_heading_boost(text):
    if not text.strip():
        return 0
    score = 0
    letter_count = sum(1 for c in text if c.isalpha())
    uppercase_ratio = sum(1 for c in text if c.isupper()) / max(letter_count, 1)
    if uppercase_ratio > 0.6:
        score += 1
    if len(text) < 60:
        score += 1
    if bool(re.match(r"^([\dA-Za-z\u0600-\u06FF\u4e00-\u9fff]+)(\.\d+)*[\s\-\:]", text)):
        score += 1
    return score

def score_heading_candidate(block, avg_font_size=12.0):
    score = 0
    text = block['text']
    font_size = block['font_size']
    
    # Relative font size heuristic
    if font_size > avg_font_size * 1.2:
        score += 2
    elif font_size > avg_font_size:
        score += 1

    if block['is_bold']:
        score += 1
    if len(text) < 60:
        score += 1
    if text.isupper():
        score += 1
    if block['x'] < 100:
        score += 1
    if not any(p in text for p in ['.', ',', ';']):
        score += 1
    if block['y'] < 200 and block['page'] == 1:
        score += 1
    if len(text) > 100:
        score -= 1
    if text.istitle():
        score += 1
    if re.match(r"^([A-Za-z]|\d+)(\.\d+)*[\s\-\:]", text):
        score += 2

    score += multilingual_heading_boost(text)

    return score