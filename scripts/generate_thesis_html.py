"""Generate a publication-quality, self-contained, printable HTML document of the 20,000+ word thesis.
Includes academic typography, embedded images with base64 fallbacks/relative links,
formatted tables, code snippets, mathematical callouts, and print media CSS for 1-click PDF export.
"""
import base64
import re
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parent.parent
MASTER_THESIS_PATH = REPO_ROOT / "docs" / "THESIS.md"
OUTPUT_HTML_PATH = REPO_ROOT / "docs" / "Financial_Stress_Detection_Thesis_Gamage_Sasini_Udeshika.html"
FIGURES_DIR = REPO_ROOT / "reports" / "figures"

def image_to_base64(path):
    if path.exists():
        with open(path, "rb") as img_file:
            return base64.b64encode(img_file.read()).decode("utf-8")
    return ""

def markdown_to_html(md_text):
    # Protect code blocks
    code_blocks = []
    def save_code_block(match):
        lang = match.group(1) or ""
        code = match.group(2)
        idx = len(code_blocks)
        escaped_code = code.replace("&", "&amp;").replace("<", "&lt;").replace(">", "&gt;")
        code_blocks.append(f"<pre class='code-block {lang}'><code>{escaped_code}</code></pre>")
        return f"___CODE_BLOCK_{idx}___"

    text = re.sub(r'```([a-zA-Z0-9_-]*)\n(.*?)```', save_code_block, md_text, flags=re.DOTALL)

    # Protect inline code
    inline_codes = []
    def save_inline_code(match):
        idx = len(inline_codes)
        code = match.group(1).replace("&", "&amp;").replace("<", "&lt;").replace(">", "&gt;")
        inline_codes.append(f"<code>{code}</code>")
        return f"___INLINE_CODE_{idx}___"

    text = re.sub(r'`([^`]+)`', save_inline_code, text)

    # Tables
    def parse_table(match):
        table_str = match.group(0).strip()
        lines = [line.strip() for line in table_str.split("\n") if line.strip()]
        if len(lines) < 2:
            return table_str
        
        headers = [c.strip() for c in lines[0].strip("|").split("|")]
        # separator line is lines[1]
        html_rows = []
        for line in lines[2:]:
            cells = [c.strip() for c in line.strip("|").split("|")]
            cell_html = "".join([f"<td>{c}</td>" for c in cells])
            html_rows.append(f"<tr>{cell_html}</tr>")
        
        header_html = "".join([f"<th>{h}</th>" for h in headers])
        return (
            "<div class='table-container'>"
            "<table class='academic-table'>"
            f"<thead><tr>{header_html}</tr></thead>"
            f"<tbody>{''.join(html_rows)}</tbody>"
            "</table></div>"
        )

    text = re.sub(r'(\|.+\|\n\|[- :|]+\|\n(?:\|.+\|\n?)+)', parse_table, text)

    # Images: ![alt](path)
    def parse_image(match):
        alt = match.group(1)
        src = match.group(2)
        img_name = Path(src).name
        local_img = FIGURES_DIR / img_name
        
        if local_img.exists():
            b64_data = image_to_base64(local_img)
            img_tag = f"<img src='data:image/png;base64,{b64_data}' alt='{alt}' />"
        else:
            img_tag = f"<img src='{src}' alt='{alt}' />"
            
        return f"<figure class='academic-figure'>{img_tag}<figcaption>{alt}</figcaption></figure>"

    text = re.sub(r'!\[(.*?)\]\((.*?)\)', parse_image, text)

    # Callouts
    def parse_alert(match):
        kind = match.group(1).upper()
        body = match.group(2).strip()
        return f"<div class='alert-card alert-{kind.lower()}'><strong>[{kind}]</strong> {body}</div>"

    text = re.sub(r'>\s*\[!(NOTE|TIP|IMPORTANT|WARNING|CAUTION)\]\s*\n((?:>.*?\n?)+)', 
                  lambda m: parse_alert(re.match(r'>\s*\[!(NOTE|TIP|IMPORTANT|WARNING|CAUTION)\]\s*\n((?:>.*?\n?)+)', m.group(0))), 
                  text)

    # Headings
    text = re.sub(r'^#### (.*?)$', r'<h4>\1</h4>', text, flags=re.MULTILINE)
    text = re.sub(r'^### (.*?)$', r'<h3>\1</h3>', text, flags=re.MULTILINE)
    text = re.sub(r'^## (.*?)$', r'<h2>\1</h2>', text, flags=re.MULTILINE)
    text = re.sub(r'^# (.*?)$', r'<h1>\1</h1>', text, flags=re.MULTILINE)

    # Bold and Italics
    text = re.sub(r'\*\*\*(.*?)\*\*\*', r'<strong><em>\1</em></strong>', text)
    text = re.sub(r'\*\*(.*?)\*\*', r'<strong>\1</strong>', text)
    text = re.sub(r'\*(.*?)\*', r'<em>\1</em>', text)

    # Blockquotes
    def parse_blockquote(match):
        bq_lines = [l.lstrip('> ').strip() for l in match.group(0).split('\n')]
        return f"<blockquote>{' '.join(bq_lines)}</blockquote>"

    text = re.sub(r'(?:^>.*$\n?)+', parse_blockquote, text, flags=re.MULTILINE)

    # Horizontal rules
    text = re.sub(r'^---+$', r'<hr class="page-divider" />', text, flags=re.MULTILINE)

    # Paragraphs
    paragraphs = text.split("\n\n")
    processed_paragraphs = []
    for p in paragraphs:
        p_stripped = p.strip()
        if not p_stripped:
            continue
        if any(p_stripped.startswith(tag) for tag in [
            "<h1", "<h2", "<h3", "<h4", "<div", "<table", "<figure", "<hr", "<blockquote", "___CODE_BLOCK"
        ]):
            processed_paragraphs.append(p_stripped)
        elif p_stripped.startswith("- ") or p_stripped.startswith("* "):
            items = [re.sub(r'^[-*]\s+', '', item) for item in p_stripped.split("\n") if item.strip()]
            list_html = "".join([f"<li>{item}</li>" for item in items])
            processed_paragraphs.append(f"<ul class='academic-list'>{list_html}</ul>")
        elif re.match(r'^\d+\.\s+', p_stripped):
            items = [re.sub(r'^\d+\.\s+', '', item) for item in p_stripped.split("\n") if item.strip()]
            list_html = "".join([f"<li>{item}</li>" for item in items])
            processed_paragraphs.append(f"<ol class='academic-list'>{list_html}</ol>")
        else:
            processed_paragraphs.append(f"<p>{p_stripped}</p>")

    text = "\n\n".join(processed_paragraphs)

    # Restore code blocks and inline code
    for i, block in enumerate(code_blocks):
        text = text.replace(f"___CODE_BLOCK_{i}___", block)
    for i, code in enumerate(inline_codes):
        text = text.replace(f"___INLINE_CODE_{i}___", code)

    return text

def build_html_document(body_html):
    return f"""<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8" />
<meta name="viewport" content="width=device-width, initial-scale=1.0" />
<title>An Intelligent Financial Stress Detection System Using User Spending Behavior — BSc (Hons) Thesis</title>
<style>
  @import url('https://fonts.googleapis.com/css2?family=Cinzel:wght@600;700&family=Lora:ital,wght@0,400;0,600;0,700;1,400&family=Inter:wght@400;500;600;700&family=JetBrains+Mono:wght@400;500&display=swap');

  :root {{
    --font-serif: 'Lora', 'Georgia', 'Times New Roman', serif;
    --font-sans: 'Inter', -apple-system, BlinkMacSystemFont, sans-serif;
    --font-mono: 'JetBrains Mono', monospace;
    --font-title: 'Cinzel', serif;
    --primary: #1B365D;
    --primary-light: #2563EB;
    --accent: #0D9488;
    --text-main: #1E293B;
    --text-muted: #475569;
    --bg-page: #F8FAFC;
    --bg-paper: #FFFFFF;
    --border: #CBD5E1;
    --line-height: 1.75;
  }}

  * {{
    box-sizing: border-box;
  }}

  body {{
    margin: 0;
    padding: 0;
    background-color: var(--bg-page);
    color: var(--text-main);
    font-family: var(--font-serif);
    font-size: 15.5px;
    line-height: var(--line-height);
  }}

  .document-container {{
    max-width: 920px;
    margin: 40px auto;
    background: var(--bg-paper);
    padding: 70px 85px;
    box-shadow: 0 4px 25px rgba(0, 0, 0, 0.07);
    border-radius: 4px;
    border: 1px solid var(--border);
  }}

  h1, h2, h3, h4 {{
    font-family: var(--font-sans);
    color: var(--primary);
    font-weight: 700;
    line-height: 1.3;
  }}

  h1 {{
    font-size: 26px;
    margin-top: 45px;
    margin-bottom: 20px;
    border-bottom: 2px solid var(--primary);
    padding-bottom: 8px;
    letter-spacing: -0.01em;
  }}

  h2 {{
    font-size: 21px;
    margin-top: 35px;
    margin-bottom: 14px;
    color: #0F172A;
    border-bottom: 1px solid #E2E8F0;
    padding-bottom: 6px;
  }}

  h3 {{
    font-size: 17.5px;
    margin-top: 26px;
    margin-bottom: 10px;
    color: #1E293B;
  }}

  h4 {{
    font-size: 15.5px;
    margin-top: 20px;
    margin-bottom: 8px;
    color: #334155;
  }}

  p {{
    margin: 0 0 16px 0;
    text-align: justify;
    text-justify: inter-word;
  }}

  strong {{
    font-weight: 600;
    color: #0F172A;
  }}

  em {{
    font-style: italic;
  }}

  blockquote {{
    border-left: 4px solid var(--accent);
    padding: 12px 20px;
    margin: 20px 0;
    background: #F0FDFA;
    font-style: italic;
    color: #0F766E;
    border-radius: 0 4px 4px 0;
  }}

  .academic-list {{
    margin: 0 0 20px 25px;
    padding: 0;
  }}

  .academic-list li {{
    margin-bottom: 8px;
    text-align: justify;
  }}

  .table-container {{
    overflow-x: auto;
    margin: 25px 0;
  }}

  .academic-table {{
    width: 100%;
    border-collapse: collapse;
    font-family: var(--font-sans);
    font-size: 13.5px;
    line-height: 1.5;
  }}

  .academic-table th, .academic-table td {{
    border: 1px solid var(--border);
    padding: 10px 12px;
    text-align: left;
    vertical-align: top;
  }}

  .academic-table th {{
    background-color: #F1F5F9;
    color: var(--primary);
    font-weight: 600;
  }}

  .academic-table tr:nth-child(even) {{
    background-color: #F8FAFC;
  }}

  .academic-figure {{
    margin: 30px auto;
    text-align: center;
  }}

  .academic-figure img {{
    max-width: 100%;
    height: auto;
    border-radius: 4px;
    border: 1px solid var(--border);
    box-shadow: 0 2px 8px rgba(0, 0, 0, 0.05);
  }}

  .academic-figure figcaption {{
    font-family: var(--font-sans);
    font-size: 13px;
    color: var(--text-muted);
    margin-top: 10px;
    font-weight: 500;
  }}

  .code-block {{
    background: #0F172A;
    color: #E2E8F0;
    font-family: var(--font-mono);
    font-size: 12.5px;
    padding: 16px 20px;
    border-radius: 6px;
    overflow-x: auto;
    margin: 20px 0;
    line-height: 1.5;
  }}

  code {{
    font-family: var(--font-mono);
    font-size: 13px;
    background: #F1F5F9;
    color: #B91C1C;
    padding: 2px 5px;
    border-radius: 3px;
  }}

  .alert-card {{
    padding: 14px 18px;
    border-radius: 6px;
    margin: 20px 0;
    font-family: var(--font-sans);
    font-size: 14px;
    line-height: 1.6;
  }}

  .alert-important {{
    background: #EFF6FF;
    border-left: 4px solid var(--primary-light);
    color: #1E3A8A;
  }}

  .alert-warning {{
    background: #FFFBEB;
    border-left: 4px solid #D97706;
    color: #92400E;
  }}

  .alert-note {{
    background: #F8FAFC;
    border-left: 4px solid #64748B;
    color: #334155;
  }}

  .page-divider {{
    border: 0;
    height: 1px;
    background: #CBD5E1;
    margin: 40px 0;
  }}

  @media print {{
    body {{
      background: #FFFFFF;
      font-size: 12pt;
    }}
    .document-container {{
      max-width: 100%;
      margin: 0;
      padding: 0;
      box-shadow: none;
      border: none;
    }}
    h1 {{
      page-break-before: always;
      margin-top: 0;
      padding-top: 20pt;
    }}
    .page-divider {{
      display: none;
    }}
  }}
</style>
</head>
<body>
  <div class="document-container">
    {body_html}
  </div>
</body>
</html>"""

def main():
    print("Reading master markdown thesis...")
    raw_md = MASTER_THESIS_PATH.read_text(encoding="utf-8")
    print("Converting Markdown to publication-styled HTML...")
    body_html = markdown_to_html(raw_md)
    full_html = build_html_document(body_html)
    OUTPUT_HTML_PATH.write_text(full_html, encoding="utf-8")
    print(f"Generated standalone HTML document: {OUTPUT_HTML_PATH}")
    print(f"Document size: {len(full_html):,d} bytes")

if __name__ == "__main__":
    main()
