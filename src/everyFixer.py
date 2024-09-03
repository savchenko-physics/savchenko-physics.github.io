import re
import os
import glob

def extract_number_from_path(file_path):
    match = re.search(r'\\\d+\.(\d+)\.', file_path)
    if match:
        return str(match.group(1))
    else:
        return None


def find_and_replace(file_path, old_word, new_word):
    try:
        with open(file_path, 'r', encoding='utf-8') as file:
            content = file.read()

        # Use regular expression to find and replace the word
        # modified_content = re.sub(r'\b' + re.escape(old_word) + r'\b', new_word, content)
        
        # new_word = '<a href="../#'+extract_number_from_path(file_path)+'">←Назад</a>'
        
        modified_content = content.replace(old_word, new_word)

        if modified_content != content:
            print(file_path, new_word)

        with open(file_path, 'w', encoding='utf-8') as file:
            file.write(modified_content)

        # print(f"Word '{old_word}' replaced with '{new_word}' in {file_path}")

    except FileNotFoundError:
        print(f"Error: File not found - {file_path}")
    except Exception as e:
        print(f"An error occurred: {e}")

def find_pdfs(directory='.'):
    pdf_files = []
    for root, dirs, files in os.walk(directory):
        for file in files:
            if file.endswith('.html'):
                pdf_files.append(os.path.join(root, file))
    return pdf_files


current_folder = 'C:\\Users\\melnichenkaa\\OneDrive - Berea College\\Documents\\GitHub\\savchenko-physics.github.io'  # Change this to the desired folder path
pdf_files_list = find_pdfs(current_folder)

new_word = """savchenkosolutions.com"""
old_word = """savchenko-physics.github.io"""


for pdf_file in pdf_files_list:
    find_and_replace(pdf_file, old_word, new_word)