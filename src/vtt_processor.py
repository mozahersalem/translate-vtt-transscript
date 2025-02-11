import os
from docx import Document

def process_vtt(input_vtt_path, output_vtt_path, docx_path):
    # Check if the input VTT file exists
    if not os.path.exists(input_vtt_path):
        print(f"Error: The file {input_vtt_path} does not exist.")
        return

    # Step 1: Duplicate the VTT file and remove specific lines
    with open(input_vtt_path, 'r', encoding='utf-8') as file:
        lines = file.readlines()

    filtered_lines = []
    skip_next_lines = 0

    for i, line in enumerate(lines):
        if line.strip() == "WEBVTT":
            continue
        if line.strip() == "":
            continue
        if line.strip().isdigit():
            continue
        if "-->" in line:
            continue
        filtered_lines.append(line)

    with open(output_vtt_path, 'w', encoding='utf-8') as file:
        file.writelines(filtered_lines)

    # Step 2: Save the modified content as DOCX
    doc = Document()
    for line in filtered_lines:
        doc.add_paragraph(line.strip())
    doc.save(docx_path)

    print(f"Files saved as: {docx_path}")