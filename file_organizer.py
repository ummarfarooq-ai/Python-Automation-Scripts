import os
import shutil

def organize_files(folder_path):
    for filename in os.listdir(folder_path):
        if filename.endswith(".txt"):
            os.makedirs("Text_Files", exist_ok=True)
            shutil.move(filename, f"Text_Files/{filename}")

        elif filename.endswith(".jpg"):
            os.makedirs("Images", exist_ok=True)
            shutil.move(filename, f"Images/{filename}")

    print("Files organized successfully.")

if __name__ == "__main__":
    organize_files(".")
