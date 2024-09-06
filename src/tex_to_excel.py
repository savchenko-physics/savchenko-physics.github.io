import re
import pandas as pd

def extract_items_to_excel(latex_file: str, excel_file: str):
    # Step 1: Open the LaTeX file and read its contents with UTF-8 encoding
    try:
        with open(latex_file, 'r', encoding='utf-8') as file:
            latex_content = file.read()
    except UnicodeDecodeError as e:
        print(f"Error reading the file: {e}")
        return

    # Step 2: Remove any image-related content between \begin{center} and \end{center} that includes \includegraphics
    latex_content = re.sub(r'\\begin{center}.*?\\includegraphics.*?\\end{center}', '', latex_content, flags=re.DOTALL)

    # Step 3: Remove any references like "Image 1.1.13"
    latex_content = re.sub(r'Image \d+\.\d+\.\d+', '', latex_content)

    # Step 4: Use regular expressions to capture section labels and items
    section_pattern = re.compile(r'\\begin{enumerate}\[label=(\d+\.\d+)\.[^]]*\]')  # Matches section label like 1.2
    item_pattern = re.compile(r'\\item\s+(.*?)(?=\\item|\\end{enumerate})', re.DOTALL)  # Matches item content

    # Step 5: Find all sections and their items
    sections = section_pattern.split(latex_content)  # Split the content by sections
    data = []

    # Process each section
    for i in range(1, len(sections), 2):  # Section labels are in odd indices
        section_label = sections[i]  # Capture section label (e.g., 1.2)
        section_content = sections[i+1]  # Corresponding section content

        # Extract each item and its content
        items = item_pattern.findall(section_content)
        for idx, item in enumerate(items, 1):  # Item numbers start from 1
            item_number = f"{section_label}.{idx}"  # Combine section and item number
            cleaned_item = item.strip()  # Clean up leading/trailing spaces
            data.append([item_number, cleaned_item])  # Append to data list

    # Step 6: Save to Excel using pandas
    df = pd.DataFrame(data, columns=['Item Number', 'Statement'])
    df.to_excel(excel_file, index=False)

    print(f"Extracted {len(data)} items and saved to {excel_file}")

# Example usage:
extract_items_to_excel('database/main.tex', 'database/output.xlsx')
