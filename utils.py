def classify_heading_level(font_size, size_level_map):
    if font_size == size_level_map.get("H1"):
        return "H1"
    elif font_size == size_level_map.get("H2"):
        return "H2"
    elif font_size == size_level_map.get("H3"):
        return "H3"
    return None

def cluster_font_sizes(font_sizes):
    font_sizes = sorted(set(font_sizes), reverse=True)
    size_map = {}
    if len(font_sizes) > 0:
        size_map["H1"] = font_sizes[0]
    if len(font_sizes) > 1:
        size_map["H2"] = font_sizes[1]
    if len(font_sizes) > 2:
        size_map["H3"] = font_sizes[2]
    return size_map