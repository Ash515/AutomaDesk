import os
import shutil

def organize_files(folder_path):
    
    files = os.listdir(folder_path)

    
    file_dict = {}

    
    for file in files:
       
        if os.path.isdir(os.path.join(folder_path, file)) or file.startswith("."):
            continue

        
        filename, extension = os.path.splitext(file)

        
        if extension[1:] not in file_dict:
            file_dict[extension[1:]] = []

        
        file_dict[extension[1:]].append(file)

    
    for extension, files in file_dict.items():
       
        extension_folder = os.path.join(folder_path, extension)
        if not os.path.exists(extension_folder):
            os.mkdir(extension_folder)

        
        for file in files:
            shutil.move(
                os.path.join(folder_path, file),
                os.path.join(extension_folder, file)
            )
