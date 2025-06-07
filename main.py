import os
import pathlib
import shutil
from os import listdir

source_folder = input("Folder to be sorted:")

current_file_types = []

for file in listdir(source_folder):
    file_name, file_type= os.path.splitext(file)
    current_file_types.append(file_type)
    for folder_file_type in current_file_types:
        try:
            full_file_path = os.path.join(source_folder, folder_file_type)
            os.mkdir(full_file_path)
            print(f"Created Folder: '{folder_file_type}': Folder location: {full_file_path}")
            moving_file = os.path.join(source_folder, file)
            shutil.move(moving_file, full_file_path)
            print(f"Moved '{file}' to '{full_file_path}'")
        except FileExistsError as e:
            continue