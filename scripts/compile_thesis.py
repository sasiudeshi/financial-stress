"""Compile individual thesis chapters into a single master THESIS.md file
and verify the word counts across each chapter and the total document.
"""
import re
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parent.parent
THESIS_DIR = REPO_ROOT / "docs" / "thesis"
MASTER_THESIS_PATH = REPO_ROOT / "docs" / "THESIS.md"

CHAPTER_FILES = [
    "00_Front_Matter.md",
    "Chapter_01_Introduction.md",
    "Chapter_02_Objectives.md",
    "Chapter_03_Literature_Review.md",
    "Chapter_04_Methodology.md",
    "Chapter_05_Results.md",
    "Chapter_06_Discussion_and_Conclusions.md",
    "99_Back_Matter_References_Appendices.md"
]

def count_words(text):
    # Remove markdown code blocks and HTML comments for clean word counting
    clean_text = re.sub(r'```.*?```', '', text, flags=re.DOTALL)
    clean_text = re.sub(r'<.*?>', ' ', clean_text)
    words = re.findall(r'\b[A-Za-z0-9_-]+\b', clean_text)
    return len(words)

def main():
    total_words = 0
    compiled_content = []

    print("=" * 70)
    print("HONOURS THESIS COMPILATION & WORD COUNT VERIFICATION")
    print("=" * 70)

    for filename in CHAPTER_FILES:
        filepath = THESIS_DIR / filename
        if not filepath.exists():
            print(f"Error: {filepath} does not exist!")
            return

        content = filepath.read_text(encoding="utf-8")
        word_count = count_words(content)
        total_words += word_count

        compiled_content.append(content)
        compiled_content.append("\n\n<div style='page-break-after: always;'></div>\n\n---\n\n")

        print(f"  {filename:48} : {word_count:6,d} words")

    print("-" * 70)
    print(f"  TOTAL THESIS WORD COUNT{'':23} : {total_words:6,d} words")
    print("=" * 70)

    master_text = "".join(compiled_content)
    MASTER_THESIS_PATH.write_text(master_text, encoding="utf-8")
    print(f"\nMaster thesis written to: {MASTER_THESIS_PATH}")
    print(f"Total file size: {len(master_text):,d} bytes")

    if total_words >= 20000:
        print("\nSUCCESS: Total word count exceeds the 20,000-word target!")
    else:
        print(f"\nWARNING: Total word count is {total_words:,d}, which is below 20,000.")

if __name__ == "__main__":
    main()
