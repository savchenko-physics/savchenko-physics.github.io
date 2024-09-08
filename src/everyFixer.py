import re
import os
import glob

def extract_number_from_path(file_path):
    numbers = file_path.split('.')
    # numbers = [int(num) for num in numbers]
    print(numbers)
    return 1


def get_nth_number(path: str, n: int) -> int:
    # Use regex to find all numbers in the path
    numbers = re.findall(r'\d+', path)

    # Convert the numbers to integers
    numbers = [int(num) for num in numbers]

    # Return the nth number (adjusting for 0-based index)
    if n > 0 and n <= len(numbers):
        return numbers[n - 1]  # n is 1-based, so subtract 1
    else:
        raise IndexError("Index out of range. The path contains fewer than {} numbers.".format(n))


def find_and_replace(file_path, old_word, new_word):
    try:
        with open(file_path, 'r', encoding='utf-8') as file:
            content = file.read()
        print("\n\n")
        print(file_path)
        old_word=f"""<a href="../#{get_nth_number(file_path, 3)}">←Назад</a>"""
        new_word = f"""<a href="../../ru#{get_nth_number(file_path, 2)}.{get_nth_number(file_path, 3)}">←Назад</a>"""
        print(old_word)
        # Use regular expression to find and replace the word
        # modified_content = re.sub(r'\b' + re.escape(old_word) + r'\b', new_word, content)
        # new_word = '<a href="../#' + extract_number_from_path(file_path) + '">←Назад</a>'
        # new_word = '<a href="../#'+extract_number_from_path(file_path)+'">←Назад</a>'
        #
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
                full_path = os.path.join(root, file)
                if full_path.count('\\') == 9:
                    pdf_files.append(full_path)
    return pdf_files

current_folder = os.getcwd().replace("src", "")

old_word = """<h3 dsadaid="back-link"><a href="../"""
new_word = """<h3 id="back-link"><a href="../../"""
pdf_files_list = []
for i in range(1,15):
    pdf_files_list += find_pdfs(f"C:\\Users\\melnichenkaa\\OneDrive - Berea College\\Documents\\GitHub\\savchenko-physics.github.io\\{i}")

for pdf_file in pdf_files_list:
    find_and_replace(pdf_file, old_word, new_word)