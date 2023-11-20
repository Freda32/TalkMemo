import re

# Read the text from a file
with open('./input/input1.txt', 'r', encoding='utf-8') as file:
    text = file.read()

# Remove timestamps and transcriber notes
cleaned_text = re.sub(r'Unknown \d+:\d+\s', '', text)
cleaned_text = re.sub(r"\bUnknown \d+:\d+\b", "", text)
# Replace multiple spaces with a single space
cleaned_text = re.sub(r"\s+", " ", text).strip()
cleaned_text = re.sub(r'Transcribed by https://otter\.ai', '', cleaned_text)

# Write the cleaned text to a new file
with open('./output/output1.txt', 'w', encoding='utf-8') as file:
    file.write(cleaned_text)

print("The cleaned text has been written to output.txt")
