import os
import shutil

source_folder = r"C:\AI PROJECTS\codealpha_tasks\source_folder"
destination_folder = r"C:\AI PROJECTS\codealpha_tasks\jpg_images"


if not os.path.exists(destination_folder):
    os.makedirs(destination_folder, exist_ok=True)


for file in os.listdir(source_folder):
    if file.lower().endswith(".jpg"):
        shutil.move(os.path.join(source_folder, file), os.path.join(destination_folder, file))
        print(f"Moved: {file}")

print("All .jpg files moved successfully!")
