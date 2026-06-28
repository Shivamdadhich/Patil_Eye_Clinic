import os
from PIL import Image

image_path = "static/client_images/client_img_19.jpeg"
output_path = "static/client_images/logo_transparent.png"

try:
    img = Image.open(image_path)
    w, h = img.size
    
    # 1. Crop out the bottom text
    # The logo icon (eye/lotus) is in the upper half of the image.
    # Let's crop from y = 0 to y = h * 0.65
    crop_box = (0, 0, w, int(h * 0.65))
    cropped_img = img.crop(crop_box)
    
    # 2. Make it transparent by replacing the background color (near-black/dark grey)
    cropped_img = cropped_img.convert("RGBA")
    datas = cropped_img.getdata()
    newData = []
    
    # Let's check what the background color is (typically at coordinates 10, 10)
    bg_sample = cropped_img.getpixel((10, 10))
    print(f"Background sample color: {bg_sample}")
    
    # If the pixel is close to the background color, make it transparent.
    # The background in the screenshot is very dark grey/black.
    for item in datas:
        # Check if the pixel is dark (R, G, B are all < 45)
        # Or close to the background sample color
        diff = abs(item[0] - bg_sample[0]) + abs(item[1] - bg_sample[1]) + abs(item[2] - bg_sample[2])
        if diff < 60 or (item[0] < 45 and item[1] < 45 and item[2] < 45):
            newData.append((255, 255, 255, 0))
        else:
            newData.append(item)
            
    cropped_img.putdata(newData)
    
    # 3. Auto-crop transparent boundaries (remove extra empty margins)
    bbox = cropped_img.getbbox()
    if bbox:
        cropped_img = cropped_img.crop(bbox)
        
    # Save as PNG
    cropped_img.save(output_path, "PNG")
    print("Logo cropped and transparency applied successfully to", output_path)
except Exception as e:
    print("Error cropping logo:", e)
