import os
from PIL import Image

directory = "static/client_images"
files = [f for f in os.listdir(directory) if f.endswith(".jpeg")]
files.sort(key=lambda x: int(x.split("_")[-1].split(".")[0]))

print(f"{'Filename':<20} | {'Resolution':<12} | {'Aspect Ratio':<12} | {'Orientation':<12}")
print("-" * 65)

for filename in files:
    path = os.path.join(directory, filename)
    try:
        with Image.open(path) as img:
            w, h = img.size
            ratio = w / h
            orientation = "Landscape" if w > h else "Portrait" if h > w else "Square"
            print(f"{filename:<20} | {f'{w}x{h}':<12} | {f'{ratio:.2f}':<12} | {orientation:<12}")
    except Exception as e:
        print(f"Error reading {filename}: {e}")
