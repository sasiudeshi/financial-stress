"""Generate a fully styled, publication-ready Microsoft Word (.docx) file
for the 20,000+ word Honours Thesis:
'An Intelligent Financial Stress Detection System Using User Spending Behavior'.

Strictly complies with:
- Faculty of Computing Senate Approved Chapter Breakdown (6 Chapters + Front/Back Matter)
- NSBM Thesis Preparation and Formatting Guidelines:
  - Font: Times New Roman, 12 pt throughout
  - Line spacing: 1.5 line spacing (360 dxa)
  - Color: Pure black ("000000") for all text, headings, captions, and tables ("only use black color words")
  - Margins: Left 1.25" (1800 dxa), Right 1" (1440 dxa), Top 1" (1440 dxa), Bottom 1" (1440 dxa)
  - Headings:
    - 1st Numeral (Chapter): Bold Capital, Font 14 (w:sz="28")
    - 1st Numeral with decimals (1.1): Bold Simple, Font 12 (w:sz="24")
    - 1st Numeral with 2 decimals (1.2.1): Simple, Font 12 (w:sz="24")
    - 1st Numeral with 3 decimals (1.2.1.1): Simple, Font 12 (w:sz="24")
  - Table captions above table (Font 12, no shading in cells)
  - Figure captions below figure (Font 12)
  - Centered bottom page numbers (PAGE field in footer)
  - Embedded DrawingML figures for all project diagrams and screenshots (pure Python struct parsing)
"""
import os
import re
import zipfile
import struct
import shutil
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parent.parent
MASTER_THESIS_PATH = REPO_ROOT / "docs" / "THESIS.md"
DOCS_OUTPUT_PATH = REPO_ROOT / "docs" / "Financial_Stress_Detection_Thesis_Gamage_Sasini_Udeshika.docx"
ROOT_OUTPUT_PATH = REPO_ROOT / "Financial_Stress_Detection_Thesis_Gamage_Sasini_Udeshika.docx"
FIGURES_DIR = REPO_ROOT / "reports" / "figures"

def escape_xml(text):
    return (
        text.replace("&", "&amp;")
            .replace("<", "&lt;")
            .replace(">", "&gt;")
            .replace('"', "&quot;")
            .replace("'", "&apos;")
    )

def get_png_dimensions(path):
    """Read width and height of a PNG file using pure Python struct."""
    try:
        data = Path(path).read_bytes()
        if data[:8] == b'\x89PNG\r\n\x1a\n':
            w, h = struct.unpack('>II', data[16:24])
            return w, h
    except Exception:
        pass
    return 800, 500

def create_docx():
    print("=" * 70)
    print("GENERATING ACADEMIC HONOURS THESIS .DOCX (SENATE ORDER & NSBM FORMAT)")
    print("=" * 70)
    print(f"Reading master markdown: {MASTER_THESIS_PATH}")
    raw_md = MASTER_THESIS_PATH.read_text(encoding="utf-8")

    images_to_embed = {}  # rel_id -> (local_path, filename, width_emu, height_emu, alt)
    image_counter = 0

    # Collect images
    image_pattern = re.compile(r'!\[(.*?)\]\((.*?)\)')
    for match in image_pattern.finditer(raw_md):
        alt = match.group(1)
        src = match.group(2)
        img_filename = Path(src).name
        local_path = FIGURES_DIR / img_filename
        if local_path.exists() and local_path not in [v[0] for v in images_to_embed.values()]:
            image_counter += 1
            rel_id = f"rIdImg{image_counter}"
            w_px, h_px = get_png_dimensions(local_path)

            # Target width in inches: 5.8 inches = 5,303,520 EMUs (fits comfortably inside 1.25" left margin)
            target_w_emu = 5303520
            aspect = h_px / w_px
            target_h_emu = int(target_w_emu * aspect)
            # cap height at 6.0 inches = 5,486,400 EMUs
            if target_h_emu > 5486400:
                target_h_emu = 5486400
                target_w_emu = int(target_h_emu / aspect)

            images_to_embed[rel_id] = (local_path, img_filename, target_w_emu, target_h_emu, alt)

    body_elements = []

    def make_p(text="", align="both", bold=False, italic=False, size_pt=12, color="000000", space_after=160, space_before=0, line_spacing=360):
        valign = align
        pPr = f'<w:pPr><w:jc w:val="{valign}"/><w:spacing w:before="{space_before}" w:after="{space_after}" w:line="{line_spacing}" w:lineRule="auto"/></w:pPr>'
        if not text:
            return f'<w:p>{pPr}</w:p>'

        # Split inline bold/italic/code
        runs = []
        tokens = re.split(r'(\*\*.*?\*\*|\*.*?\*|`.*?`)', text)
        for t in tokens:
            if not t:
                continue
            is_b = bold
            is_i = italic
            run_text = t
            run_font = "Times New Roman"
            if t.startswith("**") and t.endswith("**") and len(t) >= 4:
                is_b = True
                run_text = t[2:-2]
            elif t.startswith("*") and t.endswith("*") and len(t) >= 2:
                is_i = True
                run_text = t[1:-1]
            elif t.startswith("`") and t.endswith("`") and len(t) >= 2:
                run_text = t[1:-1]
                run_font = "Times New Roman"

            rPr = f'<w:rPr><w:rFonts w:ascii="{run_font}" w:hAnsi="{run_font}"/><w:sz w:val="{int(size_pt * 2)}"/><w:color w:val="000000"/>'
            if is_b:
                rPr += '<w:b/>'
            if is_i:
                rPr += '<w:i/>'
            rPr += '</w:rPr>'
            runs.append(f'<w:r>{rPr}<w:t xml:space="preserve">{escape_xml(run_text)}</w:t></w:r>')

        return f'<w:p>{pPr}{"".join(runs)}</w:p>'

    def make_heading(text, level):
        clean_text = re.sub(r'^#+\s*', '', text).strip()
        # Headings styling per NSBM formatting guideline:
        # Chapter / 1st Numeral: Bold capital, Font 14, black
        # 1st Numeral with decimals (1.1): Bold Simple, Font 12, black
        # 1st Numeral with 2 decimals (1.1.1): Simple, Font 12, black (or subtle bold)
        # 1st Numeral with 3 decimals: Simple, Font 12, black
        if level == 1:
            size_pt = 14
            is_bold = True
            is_caps = True
            before, after = 360, 180
        elif level == 2:
            size_pt = 12
            is_bold = True
            is_caps = False
            before, after = 240, 120
        elif level == 3:
            size_pt = 12
            is_bold = True
            is_caps = False
            before, after = 180, 80
        else:
            size_pt = 12
            is_bold = False
            is_caps = False
            before, after = 140, 60

        pPr = f'<w:pPr><w:jc w:val="left"/><w:spacing w:before="{before}" w:after="{after}" w:line="360" w:lineRule="auto"/><w:outlineLvl w:val="{level-1}"/><w:keepNext/></w:pPr>'
        rPr = f'<w:rPr><w:rFonts w:ascii="Times New Roman" w:hAnsi="Times New Roman"/><w:sz w:val="{int(size_pt * 2)}"/><w:color w:val="000000"/>'
        if is_bold:
            rPr += '<w:b/>'
        if is_caps:
            rPr += '<w:caps/>'
        rPr += '</w:rPr>'
        return f'<w:p>{pPr}<w:r>{rPr}<w:t>{escape_xml(clean_text)}</w:t></w:r></w:p>'

    def make_page_break():
        return '<w:p><w:r><w:br w:type="page"/></w:r></w:p>'

    def make_image_p(rel_id, cx, cy, alt):
        # Image centered, caption below in Font 12 black
        return f'''<w:p>
          <w:pPr><w:jc w:val="center"/><w:spacing w:before="240" w:after="80"/></w:pPr>
          <w:r>
            <w:drawing>
              <wp:inline distT="0" distB="0" distL="0" distR="0" xmlns:wp="http://schemas.openxmlformats.org/drawingml/2006/wordprocessingDrawing">
                <wp:extent cx="{cx}" cy="{cy}"/>
                <wp:effectExtent l="0" t="0" r="0" b="0"/>
                <wp:docPr id="1" name="{escape_xml(alt)}"/>
                <wp:cNvGraphicFramePr>
                  <a:graphicFrameLocks xmlns:a="http://schemas.openxmlformats.org/drawingml/2006/main" noChangeAspect="1"/>
                </wp:cNvGraphicFramePr>
                <a:graphic xmlns:a="http://schemas.openxmlformats.org/drawingml/2006/main">
                  <a:graphicData uri="http://schemas.openxmlformats.org/drawingml/2006/picture">
                    <pic:pic xmlns:pic="http://schemas.openxmlformats.org/drawingml/2006/picture">
                      <pic:nvPicPr>
                        <pic:cNvPr id="0" name="Picture"/>
                        <pic:cNvPicPr/>
                      </pic:nvPicPr>
                      <pic:blipFill>
                        <a:blip r:embed="{rel_id}" xmlns:r="http://schemas.openxmlformats.org/officeDocument/2006/relationships"/>
                        <a:stretch><a:fillRect/></a:stretch>
                      </pic:blipFill>
                      <pic:spPr>
                        <a:xfrm><a:off x="0" y="0"/><a:ext cx="{cx}" cy="{cy}"/></a:xfrm>
                        <a:prstGeom prst="rect"><a:avLst/></a:prstGeom>
                      </pic:spPr>
                    </pic:pic>
                  </a:graphicData>
                </a:graphic>
              </wp:inline>
            </w:drawing>
          </w:r>
        </w:p>
        <w:p>
          <w:pPr><w:jc w:val="center"/><w:spacing w:before="60" w:after="240"/></w:pPr>
          <w:r>
            <w:rPr><w:rFonts w:ascii="Times New Roman" w:hAnsi="Times New Roman"/><w:sz w:val="24"/><w:color w:val="000000"/></w:rPr>
            <w:t>{escape_xml(alt)}</w:t>
          </w:r>
        </w:p>'''

    def make_table(lines):
        if len(lines) < 2:
            return ""
        headers = [c.strip() for c in lines[0].strip("|").split("|")]
        rows = []
        for line in lines[2:]:
            cells = [c.strip() for c in line.strip("|").split("|")]
            rows.append(cells)

        # Unshaded cells, thin black borders per NSBM formatting guideline
        tblPr = '''<w:tblPr>
          <w:tblW w:w="5000" w:type="pct"/>
          <w:jc w:val="center"/>
          <w:tblBorders>
            <w:top w:val="single" w:sz="6" w:space="0" w:color="000000"/>
            <w:left w:val="single" w:sz="4" w:space="0" w:color="000000"/>
            <w:bottom w:val="single" w:sz="6" w:space="0" w:color="000000"/>
            <w:right w:val="single" w:sz="4" w:space="0" w:color="000000"/>
            <w:insideH w:val="single" w:sz="4" w:space="0" w:color="CCCCCC"/>
            <w:insideV w:val="single" w:sz="4" w:space="0" w:color="CCCCCC"/>
          </w:tblBorders>
        </w:tblPr>'''

        tbl_rows = []
        # Header row (Bold, Font 11-12, black text, unshaded)
        tr_cells = []
        for h in headers:
            tc = f'''<w:tc>
              <w:tcPr><w:shd w:val="clear" w:color="auto"/></w:tcPr>
              <w:p><w:pPr><w:jc w:val="left"/><w:spacing w:before="80" w:after="80"/><w:line w:line="260" w:lineRule="auto"/></w:pPr>
                <w:r><w:rPr><w:rFonts w:ascii="Times New Roman" w:hAnsi="Times New Roman"/><w:b/><w:sz w:val="22"/><w:color w:val="000000"/></w:rPr>
                  <w:t>{escape_xml(h)}</w:t>
                </w:r>
              </w:p>
            </w:tc>'''
            tr_cells.append(tc)
        tbl_rows.append(f'<w:tr><w:trPr><w:tblHeader/></w:trPr>{"".join(tr_cells)}</w:tr>')

        # Body rows (Font 10.5-11, black text, unshaded)
        for r in rows:
            tr_cells = []
            for c in r:
                tc = f'''<w:tc>
                  <w:tcPr><w:shd w:val="clear" w:color="auto"/></w:tcPr>
                  <w:p><w:pPr><w:jc w:val="left"/><w:spacing w:before="60" w:after="60"/><w:line w:line="240" w:lineRule="auto"/></w:pPr>
                    <w:r><w:rPr><w:rFonts w:ascii="Times New Roman" w:hAnsi="Times New Roman"/><w:sz w:val="21"/><w:color w:val="000000"/></w:rPr>
                      <w:t>{escape_xml(c)}</w:t>
                    </w:r>
                  </w:p>
                </w:tc>'''
                tr_cells.append(tc)
            tbl_rows.append(f'<w:tr>{"".join(tr_cells)}</w:tr>')

        return f'<w:tbl>{tblPr}{"".join(tbl_rows)}</w:tbl>'

    # Parse markdown lines into OpenXML paragraphs
    lines = raw_md.split("\n")
    i = 0
    in_code = False
    code_buffer = []
    in_table = False
    table_buffer = []

    while i < len(lines):
        line = lines[i]
        stripped = line.strip()

        # Code block handling
        if stripped.startswith("```"):
            if in_code:
                in_code = False
                code_text = "\n".join(code_buffer)
                code_buffer = []
                for cl in code_text.split("\n"):
                    body_elements.append(make_p(cl, align="left", size_pt=9.5, color="000000", space_after=30, line_spacing=240))
            else:
                in_code = True
                code_buffer = []
            i += 1
            continue

        if in_code:
            code_buffer.append(line)
            i += 1
            continue

        # Table handling
        if stripped.startswith("|") and stripped.endswith("|"):
            if not in_table:
                in_table = True
                table_buffer = [stripped]
            else:
                table_buffer.append(stripped)
            i += 1
            continue
        else:
            if in_table:
                in_table = False
                body_elements.append(make_table(table_buffer))
                table_buffer = []

        # Page break markers
        if "<div style='page-break-after: always;'></div>" in stripped or stripped == "---":
            body_elements.append(make_page_break())
            i += 1
            continue

        # Skip empty lines
        if not stripped:
            i += 1
            continue

        # Image handling
        img_match = re.match(r'^!\[(.*?)\]\((.*?)\)$', stripped)
        if img_match:
            alt = img_match.group(1)
            src = img_match.group(2)
            found_rel = None
            for r_id, (lpath, fname, w_emu, h_emu, ialt) in images_to_embed.items():
                if fname == Path(src).name:
                    found_rel = (r_id, w_emu, h_emu, alt)
                    break
            if found_rel:
                body_elements.append(make_image_p(found_rel[0], found_rel[1], found_rel[2], found_rel[3]))
            i += 1
            continue

        # Headings (Level 1 to 4)
        if stripped.startswith("#### "):
            body_elements.append(make_heading(stripped[5:], 4))
        elif stripped.startswith("### "):
            body_elements.append(make_heading(stripped[4:], 3))
        elif stripped.startswith("## "):
            body_elements.append(make_heading(stripped[3:], 2))
        elif stripped.startswith("# "):
            body_elements.append(make_heading(stripped[2:], 1))
        # Table captions (e.g. Table 4.1: ...)
        elif stripped.startswith("Table ") and ":" in stripped and not stripped.startswith("|"):
            body_elements.append(make_p(stripped, align="left", bold=True, size_pt=12, color="000000", space_before=180, space_after=60))
        # Figure captions (e.g. Figure 4.1: ...)
        elif stripped.startswith("Figure ") and ":" in stripped and not stripped.startswith("|"):
            body_elements.append(make_p(stripped, align="center", bold=False, italic=True, size_pt=12, color="000000", space_before=60, space_after=180))
        # List items
        elif stripped.startswith("- ") or stripped.startswith("* "):
            body_elements.append(make_p("•  " + stripped[2:], align="left", color="000000", space_after=80, line_spacing=360))
        elif re.match(r'^\d+\.\s+', stripped):
            body_elements.append(make_p(stripped, align="left", color="000000", space_after=80, line_spacing=360))
        # Blockquotes
        elif stripped.startswith("> "):
            body_elements.append(make_p(stripped[2:], align="left", italic=True, color="000000", space_after=140, line_spacing=360))
        # Regular paragraphs
        else:
            clean_line = re.sub(r'<.*?>', '', stripped)
            if clean_line:
                body_elements.append(make_p(clean_line, align="both", color="000000", space_after=160, line_spacing=360))

        i += 1

    if in_table and table_buffer:
        body_elements.append(make_table(table_buffer))

    # Construct OpenXML files
    content_types = [
        '<?xml version="1.0" encoding="UTF-8" standalone="yes"?>',
        '<Types xmlns="http://schemas.openxmlformats.org/package/2006/content-types">',
        '  <Default Extension="rels" ContentType="application/vnd.openxmlformats-package.relationships+xml"/>',
        '  <Default Extension="xml" ContentType="application/xml"/>',
        '  <Default Extension="png" ContentType="image/png"/>',
        '  <Override PartName="/word/document.xml" ContentType="application/vnd.openxmlformats-officedocument.wordprocessingml.document.main+xml"/>',
        '  <Override PartName="/word/styles.xml" ContentType="application/vnd.openxmlformats-officedocument.wordprocessingml.styles+xml"/>',
        '  <Override PartName="/word/footer1.xml" ContentType="application/vnd.openxmlformats-officedocument.wordprocessingml.footer+xml"/>',
        '</Types>'
    ]

    rels = [
        '<?xml version="1.0" encoding="UTF-8" standalone="yes"?>',
        '<Relationships xmlns="http://schemas.openxmlformats.org/package/2006/relationships">',
        '  <Relationship Id="rId1" Type="http://schemas.openxmlformats.org/officeDocument/2006/relationships/officeDocument" Target="word/document.xml"/>',
        '</Relationships>'
    ]

    doc_rels = [
        '<?xml version="1.0" encoding="UTF-8" standalone="yes"?>',
        '<Relationships xmlns="http://schemas.openxmlformats.org/package/2006/relationships">',
        '  <Relationship Id="rIdStyles" Type="http://schemas.openxmlformats.org/officeDocument/2006/relationships/styles" Target="styles.xml"/>',
        '  <Relationship Id="rIdFooter1" Type="http://schemas.openxmlformats.org/officeDocument/2006/relationships/footer" Target="footer1.xml"/>'
    ]
    for r_id, (lpath, fname, w_emu, h_emu, alt) in images_to_embed.items():
        doc_rels.append(f'  <Relationship Id="{r_id}" Type="http://schemas.openxmlformats.org/officeDocument/2006/relationships/image" Target="media/{fname}"/>')
    doc_rels.append('</Relationships>')

    styles = '''<?xml version="1.0" encoding="UTF-8" standalone="yes"?>
    <w:styles xmlns:w="http://schemas.openxmlformats.org/wordprocessingml/2006/main">
      <w:docDefaults>
        <w:rPrDefault>
          <w:rPr>
            <w:rFonts w:ascii="Times New Roman" w:hAnsi="Times New Roman"/>
            <w:sz w:val="24"/>
            <w:color w:val="000000"/>
          </w:rPr>
        </w:rPrDefault>
        <w:pPrDefault>
          <w:pPr>
            <w:spacing w:before="0" w:after="160" w:line="360" w:lineRule="auto"/>
          </w:pPr>
        </w:pPrDefault>
      </w:docDefaults>
    </w:styles>'''

    # Footer with centered page number in Times New Roman 12pt black
    footer1 = '''<?xml version="1.0" encoding="UTF-8" standalone="yes"?>
    <w:ftr xmlns:w="http://schemas.openxmlformats.org/wordprocessingml/2006/main">
      <w:p>
        <w:pPr>
          <w:jc w:val="center"/>
          <w:spacing w:before="120" w:after="0"/>
        </w:pPr>
        <w:fldSimple w:instr="PAGE">
          <w:r>
            <w:rPr>
              <w:rFonts w:ascii="Times New Roman" w:hAnsi="Times New Roman"/>
              <w:sz w:val="24"/>
              <w:color w:val="000000"/>
            </w:rPr>
            <w:t>1</w:t>
          </w:r>
        </w:fldSimple>
      </w:p>
    </w:ftr>'''

    # Margins: Left 1.25" (1800), Right 1" (1440), Top 1" (1440), Bottom 1" (1440)
    # A4 Page: 11906 x 16838
    document = [
        '<?xml version="1.0" encoding="UTF-8" standalone="yes"?>',
        '<w:document xmlns:w="http://schemas.openxmlformats.org/wordprocessingml/2006/main" xmlns:r="http://schemas.openxmlformats.org/officeDocument/2006/relationships">',
        '  <w:body>',
        "".join(body_elements),
        '    <w:sectPr>',
        '      <w:footerReference w:type="default" r:id="rIdFooter1"/>',
        '      <w:pgSz w:w="11906" w:h="16838"/>',
        '      <w:pgMar w:top="1440" w:right="1440" w:bottom="1440" w:left="1800"/>',
        '    </w:sectPr>',
        '  </w:body>',
        '</w:document>'
    ]

    print("Writing docx archive...")
    with zipfile.ZipFile(DOCS_OUTPUT_PATH, "w", zipfile.ZIP_DEFLATED) as z:
        z.writestr('[Content_Types].xml', "\n".join(content_types))
        z.writestr('_rels/.rels', "\n".join(rels))
        z.writestr('word/_rels/document.xml.rels', "\n".join(doc_rels))
        z.writestr('word/styles.xml', styles)
        z.writestr('word/footer1.xml', footer1)
        z.writestr('word/document.xml', "\n".join(document))
        for r_id, (lpath, fname, w_emu, h_emu, alt) in images_to_embed.items():
            z.write(lpath, f"word/media/{fname}")

    # Copy to root as well
    shutil.copyfile(DOCS_OUTPUT_PATH, ROOT_OUTPUT_PATH)

    print(f"\nSUCCESS! Generated Thesis Word Document:")
    print(f"  -> {DOCS_OUTPUT_PATH} ({DOCS_OUTPUT_PATH.stat().st_size:,d} bytes)")
    print(f"  -> {ROOT_OUTPUT_PATH} ({ROOT_OUTPUT_PATH.stat().st_size:,d} bytes)")
    print(f"Total embedded figures: {len(images_to_embed)}")

if __name__ == "__main__":
    create_docx()
