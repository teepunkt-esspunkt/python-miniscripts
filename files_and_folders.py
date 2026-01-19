import os
import shutil

#########Ordner Wählen
# Directory in dem sich das Skript befindet
ziel_ordner = os.path.dirname(os.path.abspath(__file__))
# Directory zum selber eingeben
#ziel_ordner = r"C:\Users\USERNAME\Downloads"

def dateien_in_unterordner_schieben():
    for file in os.listdir(ziel_ordner):
        if not file.lower().endswith(".mp4"):
            continue
        src_path = os.path.join(ziel_ordner, file)

        nummer = ""
        
        for ch in file:
            if ch.isdigit():
                nummer+=ch
            else:
                break
        
        folder_name = nummer.zfill(2)
        target_folder = os.path.join(ziel_ordner, folder_name)
        dest_path = os.path.join(target_folder, file)

        shutil.copy2(src_path, dest_path)


def dateien_aus_unterordner_ziehen():
    for root, dirs, files in os.walk(ziel_ordner):
        if root == ziel_ordner:
            continue

        for file in files:
            if not file.lower().endswith(".mkv"): #only *.mkv   comment out if all files wanted
                continue #comment out for all files
            file_path = os.path.join(root, file)
            destination = os.path.join(ziel_ordner, file)

            if os.path.exists(destination):
                name, ext = os.path.splitext(file)
                counter = 1
                while os.path.exists(destination):
                    destination = os.path.join(ziel_ordner, f"{name}_{counter}{ext}")
                    counter += 1

            shutil.copy2(file_path, destination)
            #shutil.move(file_path, destination) #move

    print("done:", ziel_ordner)

def ordner_anlegen(anzahl):
    for i in range(1, anzahl+1):
        folder_name = f"{i:02d}"
        folder_path = os.path.join(ziel_ordner, folder_name)
        os.makedirs(folder_path, exist_ok=True)

    print("Done.")

def dateien_umbenennen():
    for entry in os.scandir(ziel_ordner):
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
    #ordner_anlegen(12)
    #dateien_in_unterordner_schieben()
    #dateien_umbenennen()
    #dateien_aus_unterordner_ziehen()
    print("done")