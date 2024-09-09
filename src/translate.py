import re
from deep_translator import GoogleTranslator

def translate_russian_to_english(text):
    pattern = re.compile(r'\$\$(.*?)\$\$', re.DOTALL)
    
    # Split the text into parts: (outside $$) and (inside $$)
    parts = pattern.split(text)
    
    # Initialize the translator
    translator = GoogleTranslator(source='auto', target='en')
    
    # Translate only the parts that are not inside $$
    for i in range(0, len(parts), 2):  # only translate even indices (outside $$)
        parts[i] = translator.translate(parts[i])
    
    # Reconstruct the full text, including untranslated parts within $$
    translated_text = ""
    for i in range(len(parts)):
        if i % 2 == 0:
            translated_text += parts[i]  # Translated part
        else:
            translated_text += f'\n$$ {parts[i]} $$\n'  # Untranslated math expression
            
    return translated_text

def save_to_file(translated_text, filename):
    with open(filename, 'w', encoding='utf-8') as f:
        f.write(translated_text)

def read_from_file(filename):
    with open(filename, 'r', encoding='utf-8') as f:
        return f.read()

# Import the Russian text from a .txt file
input_filename = "../../../../Desktop/russia.txt"  # Replace with your actual file path
russian_text = read_from_file(input_filename)

# Translate the text
translated_text = translate_russian_to_english(russian_text)

# Save the translated text to an English text file
output_filename = "../../../../Desktop/translated_text.txt"
save_to_file(translated_text, output_filename)

print(f"Translation completed and saved to '{output_filename}'.")
