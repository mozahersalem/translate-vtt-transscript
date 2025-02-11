import os
from fix_html_entities import fix_html_entities
from vtt_processor import process_vtt
from translate_doc import translate_doc
from vtt_merge_with_en_translation import vtt_merge_with_en_translation

# Change the current working directory to the script's directory
os.chdir(os.path.dirname(os.path.abspath(__file__)))

output_dir = os.path.abspath('../dist')
os.makedirs(output_dir, exist_ok=True)  # Ensure the folder exists

input_vtt_path = './files/transcript.vtt'
output_vtt_path = os.path.join(output_dir, 'Modified_transcript')
merged_vtt_path = os.path.join(output_dir, 'DE_EN_transcript.vtt')
docx_path = os.path.join(output_dir, 'transcript.docx')
translated_docx_path = os.path.join(output_dir, 'en-transcript.docx')
print("Processing VTT file...")

# Process the VTT file
process_vtt(input_vtt_path, output_vtt_path, docx_path)

# Translate the DOCX file
translate_doc(docx_path, translated_docx_path, target_language='en')

# Merge translated docx with the VTT file
vtt_merge_with_en_translation(input_vtt_path, merged_vtt_path, translated_docx_path)

fix_html_entities(merged_vtt_path, merged_vtt_path)
