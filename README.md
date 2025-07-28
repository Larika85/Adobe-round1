
# 📘 PDF Outline Extractor — Hackathon Submission (Round 1A)

### Challenge Theme: *Connecting the Dots Through Docs*

This solution intelligently extracts a structured outline from any PDF — including the document **title**, and all **H1, H2, H3** headings — in a clean, multilingual-aware, hierarchical JSON format.

---

## 🧠 Approach

Our approach combines **layout heuristics**, **font size clustering**, and a **score-based heading detection algorithm** to simulate how a machine would understand document structure — no hardcoded assumptions or brittle rules.

### 🧩 Key Components:

#### 1. **Layout-Aware Text Block Extraction**
- Uses [`PyMuPDF`](https://github.com/pymupdf/PyMuPDF) to extract spans with **font size**, **position**, and **style metadata**.
- Breaks content into paragraph-like blocks per line with relevant features for scoring.

#### 2. **Dynamic Font Size Clustering**
- Clusters unique font sizes across the document.
- Top 3 largest font sizes are mapped to `H1`, `H2`, `H3` **adaptively**.
  
```python
# utils.py
font_sizes = sorted(set(font_sizes), reverse=True)
size_map = {"H1": font_sizes[0], "H2": font_sizes[1], "H3": font_sizes[2]}
````

#### 3. **Score-Based Heading Detection**

Each candidate block is **scored** based on:

* Relative font size
* Boldness
* Text length (short = more likely heading)
* Capitalization (UPPERCASE / Title Case)
* Alignment (left/top of page)
* Absence of trailing punctuation
* Unicode-aware regex patterns like `1.1`, `A.2`, `一.二`

Only high-scoring blocks are considered potential headings.

#### 4. **Multilingual Pattern Support**

We use Unicode-aware regex to detect heading numbering formats in **Arabic**, **Chinese**, **Japanese**, and **Indic scripts**.

Examples:

```regex
^([\dA-Za-z\u0600-\u06FF\u4e00-\u9fff]+)(\.\d+)*[\s\-\:]
```

---

## 📂 Folder Structure

```
.
├── main.py              # Core pipeline: outline extraction
├── batch_run.py         # Batch PDF processor (entry point)
├── layout_parser.py     # Text + layout extractor
├── heading_ranker.py    # Scoring heuristics
├── utils.py             # Font clustering & level classification
├── input/               # Input PDF directory (bind-mounted)
├── output/              # Output JSON directory (bind-mounted)
├── requirements.txt     # Python dependencies
├── Dockerfile           # For reproducible execution
└── README.md            # You're reading it!
```

---

## 📦 Libraries Used

| Library             | Purpose                         |
| ------------------- | ------------------------------- |
| `PyMuPDF` (`fitz`)  | PDF layout and text parsing     |
| `re`                | Regex-based heading detection   |
| `json`, `os`, `sys` | File handling and orchestration |

---

## 🔧 Docker Instructions

### 🐳 Build the Docker Image

```bash
docker build --platform linux/amd64 -t outline_extractor:harshini .
```

### ▶️ Run the Container

```bash
docker run --rm \
  -v $(pwd)/input:/app/input \
  -v $(pwd)/output:/app/output \
  --network none \
  outline_extractor:harshini
```

This processes all `.pdf` files in `input/` and outputs `.json` files to `output/`.

---

## 🧾 Output Format

Each PDF generates a structured JSON like:

```json
{
  "title": "Understanding AI",
  "outline": [
    { "level": "H1", "text": "Introduction", "page": 1 },
    { "level": "H2", "text": "What is AI?", "page": 2 },
    { "level": "H3", "text": "History of AI", "page": 3 }
  ]
}
```

---

## ✅ Constraints & Compliance

| Requirement             | Status      |
| ----------------------- | ----------- |
| ⏱ ≤ 10s per 50-page PDF | ✅ Yes       |
| 📦 Model size ≤ 200MB   | ✅ No model  |
| 🌐 No internet required | ✅ Offline   |
| ⚙️ CPU-only (amd64)     | ✅ Compliant |

---

## ✨ Highlights

* ⚡️ Efficient: No heavy models or latency
* 🔍 Smart scoring logic based on multiple features
* 🌍 Multilingual pattern detection
* 🔩 Fully deterministic and testable via Docker

---

## 📜 License

MIT License — free for research and hackathon use.

---

## 👩‍💻 Authors

## 👷 Built by

**Team Name: Vision Forge**

- **R.K. Larika**  
- **S. Harshini**

As part of Adobe’s *“Connecting the Dots”* Hackathon challenge.

---

## 🚀 Challenge Summary

> *“What if a PDF could speak to you, surface insights, and guide your reading?”*

This solution is the **first step** in enabling smart document understanding. By accurately extracting structured outlines with multilingual support, we’re laying the foundation for a better, context-aware reading experience — paving the way for the interactive webapp in Round 1B.

Let’s redefine reading. Let's connect the dots.

