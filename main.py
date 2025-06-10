import os
import shutil
from os import listdir

source_folder = input("Folder to be sorted:")

for file in listdir(source_folder):
    file_name, file_type= os.path.splitext(file)
    full_folder_path = os.path.join(source_folder, file_type)
    moving_file = os.path.join(source_folder, file)
    if not os.path.exists(full_folder_path):
        os.mkdir(full_folder_path)
    shutil.move(moving_file, full_folder_path)