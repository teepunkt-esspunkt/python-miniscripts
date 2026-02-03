# Requirements: pip install pillow pypdf2
#put all jpgs, that should be merged into one pdf, into one folder with this script and run it.
import os
from PIL import Image
from PyPDF2 import PdfWriter, PdfReader

# === CONFIG ===
base_dir = os.path.dirname(os.path.abspath(__file__))
#base_dir = r"C:\Users\USERNAME\Downloads"
#input_folder = r"C:\path\to\your\images"   # change this
#output_pdf = r"C:\path\to\output.pdf"      # change this
input_folder = base_dir
output_pdf = os.path.join(base_dir, "output.pdf")

def allJPGto1PDF(): 
    images = []

    for file in sorted(os.listdir(input_folder)):
        if file.lower().endswith((".jpg", ".jpeg")):
            path = os.path.join(input_folder, file)
            img = Image.open(path)

            # Convert to RGB (important: JPG sometimes opens as RGBA)
            if img.mode != "RGB":
                img = img.convert("RGB")

            images.append(img)

    if not images:
        print("No JPG images found.")
    else:
        # Save first image and append the rest
        images[0].save(
            output_pdf,
            save_all=True,
            append_images=images[1:]
        )
        for img in images:
            img.close()
        print("PDF created:", output_pdf)


# # put file in same folder as this file.
def splitPDF(*page_numbers):
    input = 'filename.pdf' # specify filename
    infile = PdfReader(input, 'rb')
    output = PdfWriter()

    for i in page_numbers:
        p = infile.pages[i-1] 
        output.add_page(p)

    with open('newfile.pdf', 'wb') as f:
        output.write(f)

if __name__ == "__main__":
    #allJPGto1PDF()
    #splitPDF(1, 2, 4, 5)
    print("done")