import os
import shutil
import sys

def copy_files_to_subfolders(files_to_copy):

    subfolders = [f for f in os.listdir('.') if os.path.isdir(f)]

    for folder in subfolders:
        for file_path in files_to_copy:
            shutil.copy(file_path, folder)

if __name__ == "__main__":
    files = sys.argv[1:]
    copy_files_to_subfolders(files)
