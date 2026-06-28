import os
import glob

directory = "static/client_images"
files = glob.glob(os.path.join(directory, "*.jpeg")) + glob.glob(os.path.join(directory, "*.jpg"))

# Sort files to ensure consistency
files.sort()

print(f"Found {len(files)} image files to rename.")

for i, file_path in enumerate(files, 1):
    extension = os.path.splitext(file_path)[1]
    new_name = f"client_img_{i}{extension}"
    new_path = os.path.join(directory, new_name)
    os.rename(file_path, new_path)
    print(f"Renamed: {os.path.basename(file_path)} -> {new_name}")

print("Renaming completed successfully!")
