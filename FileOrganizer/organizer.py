from pathlib import Path
import os
import shutil

target_directory = Path("/home/sahil/Projects/File Organiser/Test Folder")

file_type_dictionary = {
    "Images" : [".png",".jpg",".jpeg"],
    "Documents" : [".pdf", ".docx", ".txt"],
    "Videos" : [".mp4", ".mkv"],
    "Audio" : [".mp3", ".wav"],
    "Archives" : [".zip", ".rar"],
    "Codes" : [".py",".ipynb", ".java", ".c", ".js", ".html", ".css"]
}

for item in target_directory.iterdir():
    if item.is_file():
        file_type = item.suffix.lower()
        for directory, extensions in file_type_dictionary.items():
            if file_type in extensions:
                os.makedirs(f"{target_directory}/{directory}",exist_ok = True)
                shutil.move(f"{target_directory}/{item.name}", f"{target_directory}/{directory}/{item.name}")
                print(f"Moved : {item.name} ----> {directory}")
                break
        
