from pathlib import Path
import os
import shutil

target_directory = Path("Test Folder")

file_type_dictionary = {
    "Images" : [".png",".jpg",".jpeg"],
    "Documents" : [".pdf", ".docx", ".doc", ".txt"],
    "Videos" : [".mp4", ".mkv"],
    "Audio" : [".mp3", ".wav"],
    "Archives" : [".zip", ".rar"],
    "Codes" : [".py",".ipynb", ".java", ".c", ".js", ".html", ".css"]
}

moved_count = 0
error_count = 0
duplicate_count = 0

def destination(item,directory):
    error = 0
    global moved_count
    global error_count
    global duplicate_count
    os.makedirs(target_directory / directory,exist_ok = True)
    if Path(target_directory / directory / item.name).exists():
        i = 1
        while Path(target_directory / directory / f"{item.stem}_{i}{item.suffix}").exists():
            i += 1
        try:
            shutil.move(target_directory / item.name, target_directory / directory / f"{item.stem}_{i}{item.suffix}")
            duplicate_count += 1
            moved_count += 1
        except Exception as e:
            error = 1
            print(f"Error: {e}")
            error_count += 1
    else:
        try:
            shutil.move(target_directory / item.name, target_directory / directory / item.name)
            moved_count += 1
        except Exception as e:
            error = 1
            print(f"Error: {e}")
            error_count += 1

    return error

def statistics():
    print("="*20 + "Statistics" + "="*20)
    print(f"Total Items Moved: {moved_count}")
    print(f"Total Error Occurred: {error_count}")
    print(f"Total Duplicates: {duplicate_count}")

def get_category(file_type,item):
    flag = 0
    for directory, extensions in file_type_dictionary.items():
        if file_type in extensions:
            flag = 1
            error = destination(item,directory)
            break
    if not flag:
        directory = "Others"
        error = destination(item,directory)
    if not error:
        print(f"Moved : {item.name} ----> {directory}")

def main():
    for item in target_directory.iterdir():
        if item.is_file():
            file_type = item.suffix.lower()
            get_category(file_type,item)
    statistics()
    

main()
