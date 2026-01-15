#simple script to pull all files out of its subfolder into script root
import os
import shutil

# Directory where the script is located
script_dir = os.path.dirname(os.path.abspath(__file__))

for root, dirs, files in os.walk(script_dir):
    if root == script_dir:
        continue

    for file in files:
        if not file.lower().endswith(".mkv"): #only *.mkv   comment out if all files wanted
            continue #comment out for all files
        file_path = os.path.join(root, file)
        destination = os.path.join(script_dir, file)

        if os.path.exists(destination):
            name, ext = os.path.splitext(file)
            counter = 1
            while os.path.exists(destination):
                destination = os.path.join(script_dir, f"{name}_{counter}{ext}")
                counter += 1

        shutil.copy2(file_path, destination)
        #shutil.move(file_path, destination) #move

print("done:", script_dir)
