import os

# Define the range of folders to create
start_year = 9
end_year = start_year

# Define the folder structure
base_path = '.'  # You can change this to your desired base path
current_folder = 'C:\\Users\\melnichenkaa\\OneDrive - Berea College\\Documents\\GitHub\\savchenko-physics.github.io\\en\\'  
for year in range(start_year, end_year + 1):

    folder_name = f"{current_folder}7.3.{year}"
    folder_path = os.path.join(base_path, folder_name)
    
    # Create the folder if it doesn't exist
    os.makedirs(folder_path, exist_ok=True)
    
    # Create an empty index.html file in the folder
    index_file_path = os.path.join(folder_path, 'index.html')
    with open(index_file_path, 'w') as file:
        pass  # Just create an empty file

print("Folders and index.html files created successfully.")
