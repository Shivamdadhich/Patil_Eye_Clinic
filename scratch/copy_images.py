import shutil
import os

src_dir = r"c:\Users\Owner\OneDrive\Desktop\Patil_Eye_Clinic\IMGS\animation_imgs"
dest_dir = r"c:\Users\Owner\OneDrive\Desktop\Patil_Eye_Clinic\static"

files = [
    ("WhatsApp Image 2026-06-28 at 20.11.16 (1).jpeg", "clinic_slide1.jpeg"),
    ("WhatsApp Image 2026-06-28 at 20.11.16.jpeg", "clinic_slide2.jpeg"),
    ("WhatsApp Image 2026-06-28 at 20.11.17.jpeg", "clinic_slide3.jpeg"),
    ("WhatsApp Image 2026-06-28 at 20.11.21 (3).jpeg", "clinic_slide4.jpeg"),
]

for src_name, dest_name in files:
    src_path = os.path.join(src_dir, src_name)
    dest_path = os.path.join(dest_dir, dest_name)
    print(f"Copying {src_path} -> {dest_path}")
    shutil.copy(src_path, dest_path)

print("Done copying files!")
