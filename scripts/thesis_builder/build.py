"""Build script to write restructured thesis chapters, compile master THESIS.md,
and report word counts across each chapter.
"""
import sys
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parent.parent.parent
THESIS_DIR = REPO_ROOT / "docs" / "thesis"
MASTER_THESIS_PATH = REPO_ROOT / "docs" / "THESIS.md"

# Import chapter modules
sys.path.insert(0, str(Path(__file__).resolve().parent))
import front_matter
import chapter1
import chapter2
import chapter3
import chapter4
import chapter5
import chapter6
import back_matter

CHAPTER_MAP = [
    ("00_Front_Matter.md", front_matter.CONTENT),
    ("Chapter_01_Introduction.md", chapter1.CONTENT),
    ("Chapter_02_Objectives.md", chapter2.CONTENT),
    ("Chapter_03_Literature_Review.md", chapter3.CONTENT),
    ("Chapter_04_Methodology.md", chapter4.CONTENT),
    ("Chapter_05_Results.md", chapter5.CONTENT),
    ("Chapter_06_Discussion_and_Conclusions.md", chapter6.CONTENT),
    ("99_Back_Matter_References_Appendices.md", back_matter.CONTENT),
]

OBSOLETE_FILES = [
    "Chapter_04_System_Requirement_Specification.md",
    "Chapter_05_Implementation_and_Architecture.md",
    "Chapter_06_Testing_and_Evaluation.md",
    "Chapter_07_Concluding_Remarks.md",
]

def count_words(text):
    import re
    # Remove code blocks and html tags
    clean_text = re.sub(r'```.*?```', '', text, flags=re.DOTALL)
    clean_text = re.sub(r'<.*?>', ' ', clean_text)
    words = re.findall(r'\b[A-Za-z0-9_-]+\b', clean_text)
    return len(words)

def main():
    print("=" * 70)
    print("WRITING RESTRUCTURED SENATE CHAPTERS TO docs/thesis/")
    print("=" * 70)

    # Clean up obsolete files
    for obs in OBSOLETE_FILES:
        obs_path = THESIS_DIR / obs
        if obs_path.exists():
            obs_path.unlink()
            print(f"  Removed obsolete: {obs}")

    total_words = 0
    compiled_parts = []

    for filename, content in CHAPTER_MAP:
        out_path = THESIS_DIR / filename
        out_path.write_text(content.strip() + "\n", encoding="utf-8")
        words = count_words(content)
        total_words += words
        compiled_parts.append(content.strip())
        compiled_parts.append("\n\n<div style='page-break-after: always;'></div>\n\n---\n\n")
        print(f"  Written: {filename:45} : {words:6,d} words")

    print("-" * 70)
    print(f"  TOTAL THESIS WORD COUNT: {total_words:6,d} words")
    print("=" * 70)

    # Write master THESIS.md
    master_text = "".join(compiled_parts)
    MASTER_THESIS_PATH.write_text(master_text, encoding="utf-8")
    print(f"Master compiled thesis written to: {MASTER_THESIS_PATH}")
    print(f"Master file size: {len(master_text):,d} bytes")

    if total_words >= 20000:
        print("\nSUCCESS: Total word count comfortably meets and exceeds 20,000 words!")
    else:
        print(f"\nWARNING: Total word count is {total_words:,d}, below 20,000.")

if __name__ == "__main__":
    main()
