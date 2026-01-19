import os
import shutil

#Choose Directoy
base_dir = os.path.dirname(os.path.abspath(__file__))
#base_dir = r"C:\Users\USERNAME\Downloads"

def copy_files_into_subfolders():
    for file in os.listdir(base_dir):
        if not file.lower().endswith(".mp4"):
            continue
        src_path = os.path.join(base_dir, file)

        number = ""
        
        for ch in file:
            if ch.isdigit():
                number+=ch
            else:
                break
        
        folder_name = number.zfill(2)
        target_folder = os.path.join(base_dir, folder_name)
        dest_path = os.path.join(target_folder, file)

        shutil.copy2(src_path, dest_path)


def pull_files_from_subfolders():
    for root, dirs, files in os.walk(base_dir):
        if root == base_dir:
            continue

        for file in files:
            if not file.lower().endswith(".mkv"): #only *.mkv   comment out if all files wanted
                continue #comment out for all files
            file_path = os.path.join(root, file)
            destination = os.path.join(base_dir, file)

            if os.path.exists(destination):
                name, ext = os.path.splitext(file)
                counter = 1
                while os.path.exists(destination):
                    destination = os.path.join(base_dir, f"{name}_{counter}{ext}")
                    counter += 1

            shutil.copy2(file_path, destination)
            #shutil.move(file_path, destination) #move

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
    #create_folders(12)
    #copy_files_into_subfolders()
    #rename_files()
    #pull_files_from_subfolders()
    print("done")
