import os
folders = input("Enter the folder names with spaces: ").split()

for folder in folders:
    files = os.listdir(folder)
    print(files)
