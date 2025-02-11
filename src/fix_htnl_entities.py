import re

def fix_html_entities(input_vtt_path, output_vtt_path):
    """Fixes HTML entities in a VTT file."""
    with open(input_vtt_path, 'r', encoding='utf-8') as file:
        content = file.read()

    # Replace HTML entities with their corresponding characters
    content = re.sub(r'&#39;', "'", content)
    content = re.sub(r'&quot;', '"', content)
    content = re.sub(r'&amp;', '&', content)
    content = re.sub(r'&lt;', '<', content)
    content = re.sub(r'&gt;', '>', content)

    with open(output_vtt_path, 'w', encoding='utf-8') as file:
        file.write(content)

    print(f"✅ Fixed HTML entities in: {output_vtt_path}")

# # Example Usage
# input_vtt_path = "/Users/salem/Documents/script translate/workspace/vtt-translation-project/src/files/DE_EN_transcript.vtt"
# output_vtt_path = "/Users/salem/Documents/script translate/workspace/vtt-translation-project/src/files/DE_EN_transcript_fixed.vtt"
# fix_html_entities(input_vtt_path, output_vtt_path)