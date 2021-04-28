import shutil, os, send2trash
from pathlib import Path

p = Path.home()

for folderName, subfolders, filenames in os.walk(p):
    print('The current folder is ' + folderName)
