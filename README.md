# OCR PDF

A Python script that adds a searchable text layer to PDF files using [ocrmypdf](https://ocrmypdf.readthedocs.io/) and [Tesseract OCR](https://github.com/tesseract-ocr/tesseract).

---

## Prerequisites

| Tool | Purpose |
|------|---------|
| **Python 3.9+** | Runtime |
| **Tesseract OCR** | OCR engine used by ocrmypdf |
| **Ghostscript** | PDF rendering (required by ocrmypdf) |

### 1. Install Tesseract OCR

Download the Windows installer from [UB-Mannheim/tesseract](https://github.com/UB-Mannheim/tesseract/wiki) and run it.

During installation:
- Note the install directory (default: `C:\Program Files\Tesseract-OCR`).
- Under **Additional language data**, select **Vietnamese** (`vie`) if you need Vietnamese OCR (the script defaults to `vie`).

After installation, add Tesseract to your system `PATH`:

```powershell
# Verify it's accessible
tesseract --version
```

> **Tip:** If you don't want to modify your system PATH, you can pass the Tesseract location at runtime with `--tesseract-path` (see [Usage](#usage)).

### 2. Install Ghostscript

Download and install from [ghostscript.com/releases](https://ghostscript.com/releases/gsdnld.html). The installer automatically adds it to PATH.

```powershell
# Verify
gswin64c --version
```

---

## Install Python Dependencies

```powershell
pip install ocrmypdf
```

This single package is the only Python dependency required.

> **Optional:** Use a virtual environment to keep your system Python clean:
> ```powershell
> python -m venv .venv
> .venv\Scripts\activate
> pip install ocrmypdf
> ```

---

## Usage

### Basic

```powershell
python ocr_pdf.py "path\to\your\file.pdf"
```

The output PDF is saved next to the input file with an `_ocr` suffix.  
For example: `document.pdf` → `document_ocr.pdf`

### Options

```
usage: ocr_pdf.py [-h] [--language LANGUAGE] [--optimize {0,1,2,3}]
                  [--tesseract-path TESSERACT_PATH]
                  [input_pdf]
```

| Option | Default | Description |
|--------|---------|-------------|
| `input_pdf` | Hardcoded path in script | Path to input PDF |
| `--language` | `vie` | Tesseract language code(s), e.g. `vie`, `eng`, or `vie+eng` |
| `--optimize` | `0` | PDF optimization level (0–3). Level 0 avoids extra dependencies. |
| `--tesseract-path` | Auto-detect via PATH | Explicit path to `tesseract.exe` or its install directory |

### Examples

```powershell
# OCR a Vietnamese PDF
python ocr_pdf.py "C:\Documents\exam.pdf"

# OCR with English language
python ocr_pdf.py "C:\Documents\exam.pdf" --language eng

# OCR with both Vietnamese and English
python ocr_pdf.py "C:\Documents\exam.pdf" --language vie+eng

# Specify Tesseract location manually
python ocr_pdf.py "C:\Documents\exam.pdf" --tesseract-path "C:\Program Files\Tesseract-OCR"
```
