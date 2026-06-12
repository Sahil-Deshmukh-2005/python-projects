from pathlib import Path
import os
import shutil

os.makedirs("Test Folder", exist_ok=True)

path = input("Enter your interested path for organization from current directory (Press ENTER for current path): ")
target_directory = Path(path)

file_type_dictionary = {
    "Images" : [".png",".jpg",".jpeg"],
    "Documents" : [".pdf", ".docx", ".doc", ".txt", ".odt"],
    "Videos" : [".mp4", ".mkv"],
    "Audio" : [".mp3", ".wav"],
    "Archives" : [".zip", ".rar", ".tar", ".apk"],
    "Codes" : [".py",".ipynb", ".java", ".c", ".js", ".html", ".css"]
}

moved_count = 0
error_count = 0
duplicate_count = 0

def destination(item,directory):
    error = 0
    global moved_count, error_count, duplicate_count
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
            with open("organizer.log","a") as f:
                f.write(f"Error, {e}, occured while moving {item.name}.")
                f.write("\n")
            error_count += 1
    else:
        try:
            shutil.move(target_directory / item.name, target_directory / directory / item.name)
            moved_count += 1
        except Exception as e:
            error = 1
            with open("organizer.log","a") as f:
                f.write(f"Error, {e}, occured while moving {item.name}.")
                f.write("\n")
            error_count += 1

    return error

def statistics():
    print("="*20 + " Statistical Data " + "="*20)
    print(f"Total Items Moved: {moved_count}")
    print(f"Total Error Occurred: {error_count}")
    print(f"Total Duplicates In Moved Items: {duplicate_count}")
    print("="*58)

def get_category(file_type):
    for directory, extensions in file_type_dictionary.items():
        if file_type in extensions:
            return directory
         
    return "Others"

def read_log():
    while True:
        response = input("Do you wanna see the log file (Y/n): ")
        if response.lower() == "y":
            with open("organizer.log","r") as f:
                lines = f.readlines()
                for line in lines:
                    print(line.strip())           
                return
        elif response.lower() == "n":
            return
        else:
            print("Enter proper response.")

def delete_log():
    while True:
        command = input("Do you wanna delete the log content (Y/n): ")
        if command.lower() == "y":
            os.remove("organizer.log")
            return
        elif command.lower() == "n":
            return
        else:
            print("Enter proper command.")

def main():
    if not target_directory.exists():
        print("File does not exist.")
        return
    
    for item in target_directory.iterdir():
        if item.is_file():
            file_type = item.suffix.lower()
            directory = get_category(file_type)
            error = destination(item,directory)
            if not error:
                with open("organizer.log","a") as f:
                    f.write(f"Moved : {item.name} ----> {directory}")
                    f.write("\n")
    statistics()
    if Path("organizer.log").exists():
        read_log()
        delete_log()
    

main()
