import os
import shutil
import re

#Choose Directoy
base_dir = os.path.dirname(os.path.abspath(__file__))
#base_dir = r"C:\Users\USERNAME\Downloads"


def fix_episode_numbers():
    for entry in os.scandir(base_dir):
        if not entry.is_file():
            continue
        name = entry.name

        match = re.search(r'\d+', name)  # first number anywhere in the name
        if not match:
            continue  # no digits at all

        number = match.group()
        if len(number) != 1:
            continue
        padded = number.zfill(2)
        new_name = re.sub(r'\d+', padded, name, count=1)

        old_path = entry.path
        new_path = os.path.join(base_dir, new_name)

        if os.path.exists(new_path):
            print(f"[WARN] Skipping rename {name} -> {new_name}, target exists")
            continue

        os.rename(old_path, new_path)
        print(f"[OK] {name} -> {new_name}")


def put_files_into_subfolders(fileext = ".mp4"):
    for file in os.listdir(base_dir):
        if not file.lower().endswith(fileext):
            continue
        source_path = os.path.join(base_dir, file)

        match = re.search(r'\d+', file)
        if not match:
            print(f"[WARN] Error {file}")
            continue

        number = match.group()
        
        folder_name = number.zfill(2)
        target_folder = os.path.join(base_dir, folder_name)
        destination_path = os.path.join(target_folder, file)

        #shutil.copy2(source_path, destination_path)
        shutil.move(source_path, destination_path)


def pull_files_from_subfolders(fileext = ".mkv"):
    for root, dirs, files in os.walk(base_dir):
        if root == base_dir:
            continue

        for file in files:
            if not file.lower().endswith(fileext): #comment out if all files wanted
                continue #comment out for all files
            source_path = os.path.join(root, file)
            destination_path = os.path.join(base_dir, file)

            if os.path.exists(destination_path):
                name, ext = os.path.splitext(file)
                counter = 1
                while os.path.exists(destination_path):
                    destination_path = os.path.join(base_dir, f"{name}_{counter}{ext}")
                    counter += 1

            #shutil.copy2(source_path, destination_path)
            shutil.move(source_path, destination_path) #move

    print("done:", base_dir)

def create_folders(amount):
    for i in range(1, amount+1):
        folder_name = f"{i:02d}"
        folder_path = os.path.join(base_dir, folder_name)
        os.makedirs(folder_path, exist_ok=True)

    print("Done.")

# name a subtitle file according to the video file. only 2 files per folder allowed (mp3 + vtt)
def rename_files():
    for entry in os.scandir(base_dir):
        if not entry.is_dir():
            continue
    
        folder = entry.path
        video_name = None
        subtitle_name = None
        
        for file in os.listdir(folder):
            if file.lower().endswith('.mp4'):
                video_name = file
            if file.lower().endswith('.vtt'):
                subtitle_name = file
                
        base, _ = os.path.splitext(video_name)
        new_name = base + ".vtt"
        old = os.path.join(folder, subtitle_name)
        new = os.path.join(folder, new_name)
        os.rename(old, new)


        

if __name__ == "__main__":
    #rename_files()
    #create_folders(12)
    #put_files_into_subfolders()
    #fix_episode_numbers()
    ###MKVtoolnix
    #pull_files_from_subfolders()
    print("done")
