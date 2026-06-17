#!/usr/bin/env python3
"""Run OCR on a PDF using ocrmypdf.

If you don't pass an input path, update INPUT_PDF below with your file.
Output PDF will be written next to the input file with "_ocr" suffix.
"""

from __future__ import annotations

import argparse
import os
import shutil
from pathlib import Path

import ocrmypdf


INPUT_PDF = r"C:\Users\thinh\Documents\HK_6\Software_Engineering\final_exam\231.pdf"  # Placeholder path


def build_output_path(input_path: Path) -> Path:
    return input_path.with_name(f"{input_path.stem}_ocr{input_path.suffix}")


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="OCR a PDF using ocrmypdf")
    parser.add_argument(
        "input_pdf",
        nargs="?",
        default=INPUT_PDF,
        help="Path to input PDF (default: placeholder in script)",
    )
    parser.add_argument(
        "--language",
        default="vie",
        help="Tesseract language(s), e.g. 'vie' or 'vie+eng'",
    )
    parser.add_argument(
        "--optimize",
        type=int,
        choices=[0, 1, 2, 3],
        default=0,
        help="Optimization level (0 disables jbig2/pngquant dependencies)",
    )
    parser.add_argument(
        "--tesseract-path",
        default=None,
        help="Path to tesseract.exe or its install directory (optional)",
    )
    return parser.parse_args()


def ensure_tesseract_on_path(explicit_path: str | None) -> None:
    if explicit_path:
        candidate = Path(explicit_path)
        if candidate.is_dir():
            os.environ["PATH"] = f"{candidate};{os.environ.get('PATH', '')}"
        else:
            if not candidate.exists():
                raise SystemExit(f"Tesseract not found at: {candidate}")
            os.environ["PATH"] = f"{candidate.parent};{os.environ.get('PATH', '')}"

    if shutil.which("tesseract") is None:
        raise SystemExit(
            "Tesseract not found on PATH. Install it and either add it to PATH "
            "or pass --tesseract-path to this script."
        )


def main() -> None:
    args = parse_args()
    input_path = Path(args.input_pdf)
    tesseract_path = args.tesseract_path or os.environ.get("TESSERACT_PATH")

    if not input_path.exists():
        raise SystemExit(f"Input PDF not found: {input_path}")

    ensure_tesseract_on_path(tesseract_path)

    output_path = build_output_path(input_path)

    # Run OCR and write output next to the input
    ocrmypdf.ocr(
        str(input_path),
        str(output_path),
        language=args.language,
        deskew=True,
        rotate_pages=True,
        force_ocr=True,
        optimize=args.optimize,
    )

    print(f"OCR complete: {output_path}")


if __name__ == "__main__":
    main()
