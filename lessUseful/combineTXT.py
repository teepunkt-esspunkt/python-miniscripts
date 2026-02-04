import os

def combine_txt_files(output_file="combined.txt"):
    # Get the directory where the script is located
    script_dir = os.path.dirname(os.path.abspath(__file__))

    # List all .txt files in the directory (excluding the output file)
    txt_files = [f for f in os.listdir(script_dir) if f.endswith(".txt") and f != output_file]

    with open(os.path.join(script_dir, output_file), "w", encoding="utf-8") as outfile:
        for filename in txt_files:
            file_path = os.path.join(script_dir, filename)
            with open(file_path, "r", encoding="utf-8") as infile:
                content = infile.read()
                outfile.write(f"--- {filename} ---\n")  # Optional: mark the file's start
                outfile.write(content + "\n\n")

    print(f"Combined {len(txt_files)} files into {output_file}.")

def combine_vtt_files(output_file="combined.vtt"):
    script_dir = os.path.dirname(os.path.abspath(__file__))

    vtt_files = sorted(
        f for f in os.listdir(script_dir)
        if f.lower().endswith(".vtt") and f != output_file
    )

    if not vtt_files:
        print("No VTT files found.")
        return

    output_path = os.path.join(script_dir, output_file)

    with open(output_path, "w", encoding="utf-8") as outfile:
        # VTT requires exactly one header
        outfile.write("WEBVTT\n\n")

        for filename in vtt_files:
            file_path = os.path.join(script_dir, filename)

            with open(file_path, "r", encoding="utf-8") as infile:
                lines = infile.readlines()

            # remove WEBVTT header if present
            if lines and lines[0].strip().upper().startswith("WEBVTT"):
                lines = lines[1:]
                if lines and lines[0].strip() == "":
                    lines = lines[1:]

            # filename marker (comment, valid in VTT)
            outfile.write(f"NOTE --- {filename} ---\n\n")

            outfile.writelines(lines)
            outfile.write("\n\n")

    print(f"Combined {len(vtt_files)} files into {output_file}.")

if __name__ == "__main__":
    #combine_txt_files()
    #combine_vtt_files()
    print("done")