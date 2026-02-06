<p align="center">
  <img src="https://img.shields.io/badge/python-3.11+-3776AB?style=for-the-badge&logo=python&logoColor=white" alt="Python 3.11+">
  <img src="https://img.shields.io/badge/Flask-000000?style=for-the-badge&logo=flask&logoColor=white" alt="Flask">
  <img src="https://img.shields.io/badge/Bioinformatics-4CAF50?style=for-the-badge&logo=dna&logoColor=white" alt="Bioinformatics">
</p>

<h1 align="center">🧬 Seer</h1>

<p align="center">
  <strong>A Bioinformatics Web Application</strong><br>
  <em>Process genomic sequences · Transform file formats · Learn bioinformatics</em>
</p>

---

## About

**Seer** is a Flask-powered web application that puts common bioinformatics tools at your fingertips. Built as a SACHS Chemistry 11 CPT, it implements well-known genomic analysis algorithms from [Rosalind](http://rosalind.info/) and provides bidirectional conversion between popular sequence file formats (Plain Text, FASTA, and EMBL).

### Demo

https://github.com/user-attachments/assets/ffac56f7-e2a7-4d5e-8cd6-8316cb73ab22

---

## Features

### Algorithms

| Algorithm | ID | Description | Input |
|---|:---:|---|---|
| **DNA → RNA Transcription** | `DRT` | Transcribes a DNA string into its RNA equivalent | DNA string |
| **Reverse Complement** | `RCD` | Returns the reverse complement of a DNA strand | DNA string |
| **Counting Nucleotides** | `CN` | Counts occurrences of each nucleotide (A, C, G, T) | DNA string |
| **GC Content** | `GC` | Computes the highest GC-content percentage from FASTA data | FASTA file |
| **Consensus & Profile Matrix** | `CSM` | Derives a consensus string and nucleotide frequency profile | FASTA file |
| **Hamming Distance** | `HD` | Counts point mutations between two equal-length DNA strings | Text file |
| **RNA → Protein** | `RNAP` | Translates an mRNA string into its protein sequence | RNA file |
| **Motif Finding** | — | Locates all positions of a substring motif within a DNA string | Text file |
| **Fibonacci (Rabbit Recurrence)** | `FI` | Models rabbit population growth across generations | _n_, _k_ values |

> **Quick Access:** Use the shortcut IDs in the homepage search bar to jump straight to an algorithm.

### File Format Conversions

| Conversion | Direction |
|---|---|
| Plain Text ↔ FASTA | Bidirectional |
| FASTA ↔ EMBL | Bidirectional |

All converted files are available for **immediate download** after processing.

---

## Project Structure

```
Seer/
├── .gitignore
├── README.md
│
├── Algorithms/                          # Standalone CLI algorithm scripts (Rosalind solutions)
│   ├── Computing GC Content
│   ├── Counting DNA Nucleotides
│   ├── Rabbits and Recurrence
│   ├── hamming.py
│   ├── motif.py
│   └── RNA-to-Protein/
│       ├── RNA-to-protein.py
│       └── table.txt                    # Codon → amino acid lookup table
│
└── Seer 1.91/                           # Main application (v1.91)
    ├── Algorithms/                      # Algorithm scripts (mirror of root)
    ├── File Conversion Algs/            # Standalone conversion scripts
    │   ├── fasta+embl/                  # FASTA ↔ EMBL converters + sample data
    │   └── fasta+plain/                 # FASTA ↔ Plain Text converters + sample data
    │
    └── Flask Web App/                   # ⭐ The web application
        ├── main.py                      # Entry point — starts the Flask server
        ├── processed-files/             # Runtime output directory (gitignored)
        └── website/
            ├── __init__.py              # App factory & blueprint registration
            ├── algorithms.py            # Algorithm route handlers & logic
            ├── conversion.py            # File conversion route handlers
            ├── download.py              # File download endpoints
            ├── search.py                # Quick-access search bar handler
            ├── views.py                 # Home page view
            ├── button.py                # Home button navigation helper
            ├── mainmenu.py              # Main menu / navigation routes
            ├── static/css/
            │   ├── style.css            # Homepage stylesheet
            │   └── algstyle.css         # Algorithm pages stylesheet
            └── templates/               # Jinja2 HTML templates
                ├── home.html
                ├── algorithms.html
                ├── conversion.html
                ├── fibonacci.html
                ├── countingnucleotides.html
                ├── gccontent.html
                ├── consensus.html
                ├── hamming.html
                ├── rnatoprotein.html
                ├── motif.html
                ├── transcription.html
                ├── complement.html
                ├── plain_fasta.html
                ├── fasta_plain.html
                ├── fasta_embl.html
                ├── embl_fasta.html
                ├── learn.html
                └── aboutus.html
```

---

## 🚀 Getting Started

### Prerequisites

- **Python 3.11+**
- **pip**

### Installation

```bash
# Clone the repository
git clone https://github.com/yourusername/Seer.git
cd Seer

# (Recommended) Create a virtual environment
python -m venv venv
source venv/bin/activate

# Install dependencies
pip install flask
```

### Running the Application

```bash
cd "Seer 1.91/Flask Web App"
python main.py
```

Open **http://localhost:3000** in your browser.

---

## 🧪 Algorithm References

Every algorithm is an implementation of a problem from [Rosalind](http://rosalind.info/), a platform for learning bioinformatics and programming:

| Problem | Rosalind Link |
|---|---|
| Counting DNA Nucleotides | [rosalind.info/problems/dna](http://rosalind.info/problems/dna/) |
| Transcribing DNA into RNA | [rosalind.info/problems/rna](http://rosalind.info/problems/rna/) |
| Complementing a Strand of DNA | [rosalind.info/problems/revc](http://rosalind.info/problems/revc/) |
| Computing GC Content | [rosalind.info/problems/gc](http://rosalind.info/problems/gc/) |
| Hamming Distance | [rosalind.info/problems/hamm](http://rosalind.info/problems/hamm/) |
| Finding a Motif in DNA | [rosalind.info/problems/subs](http://rosalind.info/problems/subs/) |
| Translating RNA into Protein | [rosalind.info/problems/prot](http://rosalind.info/problems/prot/) |
| Consensus and Profile | [rosalind.info/problems/cons](http://rosalind.info/problems/cons/) |
| Rabbits and Recurrence Relations | [rosalind.info/problems/fib](http://rosalind.info/problems/fib/) |

---

## ⚠️ Codebase Hygiene — Issues Found & Fixed

A thorough review of the repository uncovered the following software engineering issues:

### ✅ Fixed

| # | Issue | Severity |
|---|---|---|
| 1 | **No `.gitignore` file** — `.DS_Store` files, `__pycache__/` directories, `.pyc` bytecode, and generated output files were all committed to version control | 🔴 High |
| 2 | **`__pycache__/` committed** — 12 compiled `.pyc` files tracked in git, including stale caches for deleted modules (`auth`, `dropdown`, `fibonacci`) | 🔴 High |
| 3 | **Generated output files committed** — `processed-files/*.txt` are runtime artifacts and should never be in version control | 🟡 Medium |
| 4 | **`.DS_Store` files committed** — 3 macOS system files tracked at multiple directory levels | 🟡 Medium |

### ⚠️ Open — Recommended Future Fixes

| # | Issue | Severity | Recommendation |
|---|---|---|---|
| 5 | **Hardcoded absolute file paths** in `conversion.py` (e.g. `/Users/kurtisng/Documents/dev/...`) — the app will crash on any other machine | 🔴 High | Use `os.path.join(os.path.dirname(__file__), '..', 'processed-files', ...)` or Flask's `app.root_path` |
| 6 | **Path traversal vulnerability** in `download.py` — user-controlled `file` query param is passed directly to `send_file()` with zero validation | 🔴 High | Restrict downloads to the `processed-files/` directory; validate and sanitize the path |
| 7 | **Secret key hardcoded** — `app.config['SECRET_KEY'] = 'bioinformatics'` in `__init__.py` | 🟡 Medium | Load from environment variable: `os.environ.get('SECRET_KEY')` |
| 8 | **No `requirements.txt`** or `pyproject.toml` — dependency management is absent | 🟡 Medium | Add `requirements.txt` with `flask` pinned to a version |
| 9 | **No input validation** — algorithm endpoints have no `try/except` blocks; malformed uploads will produce unhandled 500 errors | 🟡 Medium | Wrap request parsing in try/except and return user-friendly error messages |
| 10 | **Duplicate `Algorithms/` folder** — the root `Algorithms/` directory is an exact copy of `Seer 1.91/Algorithms/` | 🟢 Low | Remove the duplicate |
| 11 | **`import re` unused** in `algorithms.py` — imported at the top but never used | 🟢 Low | Remove the unused import |
| 12 | **`button.py` + `views.py` serve the same route** (`/`) with the same template — redundant blueprint | 🟢 Low | Consolidate into a single home view |
| 13 | **`print("XX\n")` in `conversion.py`** line 130 — should be `f.write("XX\n")` (prints to server console instead of file) | 🟡 Medium | Change `print` → `f.write` |

---

## 📄 Documentation

- **[Project Report & References](https://drive.google.com/file/d/1vN7ej1nrN0YVqAd85SMpePdO8_ZXJkN7/view?usp=sharing)**

---

## 🛠️ Tech Stack

| Layer | Technology |
|---|---|
| **Backend** | Python, Flask |
| **Frontend** | HTML5, CSS3, Jinja2 |
| **Fonts** | Product Sans, Montserrat, Sulphur Point, Varela Round |
| **Domain** | Bioinformatics, Genomics |

---

<p align="center">
  <sub>Built with 🧬 and Flask · SACHS Chemistry 11 CPT</sub>
</p>
