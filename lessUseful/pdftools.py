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

def jpgs_to_pdfs():
    for file in sorted(os.listdir(input_folder)):
        if not file.lower().endswith((".jpg", ".jpeg")):
            continue

        jpg_path = os.path.join(input_folder, file)

        # keep name, only change extension
        pdf_name = os.path.splitext(file)[0] + ".pdf"
        pdf_path = os.path.join(input_folder, pdf_name)

        img = Image.open(jpg_path)

        if img.mode != "RGB":
            img = img.convert("RGB")

        img.save(pdf_path)
        img.close()

        print(f"[OK] {file} → {pdf_name}")

def combine_all_pdfs():
    """Combine ALL PDFs in BASE_DIR into one PDF."""
    writer = PdfWriter()

    pdf_files = sorted(
        f for f in os.listdir(input_folder)
        if f.lower().endswith(".pdf") and f != os.path.basename(output_pdf)
    )

    if not pdf_files:
        print("No PDFs found to combine.")
        return

    for pdf in pdf_files:
        reader = PdfReader(os.path.join(input_folder, pdf))
        for page in reader.pages:
            writer.add_page(page)

    with open(output_pdf, "wb") as f:
        writer.write(f)

    print(f"[OK] Combined {len(pdf_files)} PDFs → {input_folder}")


# # put file in same folder as this file.
def extractPDFs(*page_numbers):
    input = 'filename.pdf' # specify filename
    infile = PdfReader(input, 'rb')
    output = PdfWriter()

    for i in page_numbers:
        p = infile.pages[i-1] 
        output.add_page(p)

    with open('newfile.pdf', 'wb') as f:
        output.write(f)

if __name__ == "__main__":
    ##allJPGto1PDF()
    #jpgs_to_pdfs()
    combine_all_pdfs()
    #extractPDFs(1, 2, 4, 5)

    print("done")
