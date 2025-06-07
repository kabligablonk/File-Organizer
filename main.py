import os
import shutil
from os import listdir

source_folder = input("Folder to be sorted:")

current_file_types = []

for file in listdir(source_folder):
    file_name, file_type= os.path.splitext(file)
    current_file_types.append(file_type)
for folder_file_type in current_file_types:
    try:
        full_path = os.path.join(source_folder, folder_file_type)
        os.mkdir(full_path)
        print(f"Created Folder: '{folder_file_type}': Folder location: {full_path}")
    except FileExistsError as e:
        continue