import os
import shutil
from os import listdir

source_folder = "C:\\Users\\aeggn\\OneDrive\\Desktop\\Test"
destination_folder = ""

current_file_types = []

for file in listdir(source_folder):
    file_name, file_type= os.path.splitext(file)
    current_file_types.append(file_type)
for folder_file_type in current_file_types:

print(current_file_types)