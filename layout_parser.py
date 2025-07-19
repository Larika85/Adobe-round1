import fitz  # PyMuPDF

def extract_text_blocks(pdf_path):
    doc = fitz.open(pdf_path)
    all_blocks = []
    for page_number, page in enumerate(doc, start=1):
        blocks = page.get_text("dict")['blocks']
        for b in blocks:
            if 'lines' not in b:
                continue
            for line in b['lines']:
                text = ""
                max_font_size = 0
                is_bold = False
                x0, y0 = 9999, 9999
                for span in line['spans']:
                    text += span['text']
                    max_font_size = max(max_font_size, span['size'])
                    if 'bold' in span['font'].lower():
                        is_bold = True
                    x0 = min(x0, span['bbox'][0])
                    y0 = min(y0, span['bbox'][1])
                if text.strip():
                    all_blocks.append({
                        'text': text.strip(),
                        'font_size': max_font_size,
                        'is_bold': is_bold,
                        'x': x0,
                        'y': y0,
                        'page': page_number
                    })
    return all_blocks
