from docx import Document

def vtt_merge_with_en_translation(output_vtt_path, merged_vtt_path, en_docx_path):
    doc = Document(en_docx_path)
    english_lines = [p.text.strip() for p in doc.paragraphs if p.text.strip()]

    # Load German VTT file content
    with open(output_vtt_path, 'r', encoding='utf-8') as file:
        german_lines = file.readlines()

    # Initialize output lines and indices
    output_lines = []
    english_index = 0

    # Iterate over German lines
    for i, line in enumerate(german_lines):
        stripped_line = line.strip()
        output_lines.append(line)  # Preserve original line structure

        # If the line contains a dialogue (but not timestamps or headers)
        if ": " in stripped_line and "-->" not in stripped_line and not stripped_line.startswith("WEBVTT"):
            if english_index < len(english_lines):
                english_translation = english_lines[english_index]
                output_lines.append(f"{english_translation}\n")  # ✅ Append translation without extra lines
                english_index += 1

    # Add any remaining English lines (if extra translations exist)
    while english_index < len(english_lines):
        output_lines.append(f"{english_lines[english_index]}\n")
        english_index += 1

    # ✅ Ensure no extra blank lines before saving
    with open(merged_vtt_path, 'w', encoding='utf-8') as file:
        file.writelines(output_lines)

    print(f"✅ The merged file has been saved as: {merged_vtt_path}")

# Example Usage:
# output_vtt_path = 'transcript.vtt'
# merged_vtt_path = 'Combined_German_English.vtt'
# en_docx_path = 'EN-transcript.docx'
# vtt_merge_with_en_translation(output_vtt_path, merged_vtt_path, en_docx_path)