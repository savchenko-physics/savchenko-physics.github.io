import os
import re

def count(base_path):
    pattern = re.compile(r'^\d+\.\d+\.\d+$')
    unique_folders = set()

    for root, dirs, files in os.walk(base_path):
        folder_name = os.path.basename(root)
        if pattern.match(folder_name):
            if 'index.html' in files:
                unique_folders.add(folder_name)

    return len(unique_folders)
