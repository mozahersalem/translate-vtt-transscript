from docx import Document

# Define the path to the original VTT file and the output DOCX file
vtt_file_path = 'transcript.vtt'
docx_file_path = 'extracted_lines.docx'

# Lines to keep
lines_to_keep = [
    "Sabine Kurz: Entschuldigung.",
    "Sabine Kurz: So, Jetzt nehmen wir das aber auch",
    "Sabine Kurz: Ja.",
    "Sabine Kurz: und wir machen weiter mit einem positiv und einem Negativbeispiel. Das sind weiße Handtücher.",
    "Sabine Kurz: Das ist positiv.",
    "Sabine Kurz: und Jerem: Was ist negativ?",
    "Kerem Alemdar: Das sind"
]

# Create a new Document
doc = Document()

# Read the VTT file and extract the desired lines
with open(vtt_file_path, 'r', encoding='utf-8') as file:
    for line in file:
        if any(keep_line in line for keep_line in lines_to_keep):
            doc.add_paragraph(line.strip())

# Save the document
doc.save(docx_file_path)
print(f"Extracted lines saved to {docx_file_path}")