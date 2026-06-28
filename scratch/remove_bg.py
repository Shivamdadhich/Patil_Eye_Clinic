import os
from PIL import Image

image_path = "static/client_images/client_img_19.jpeg"
output_path = "static/client_images/logo_transparent.png"

try:
    img = Image.open(image_path)
    img = img.convert("RGBA")
    
    datas = img.getdata()
    newData = []
    
    # We want to replace white/near-white pixels with transparency
    # A pixel is near-white if R, G, B are all > 220
    for item in datas:
        # Check if the pixel is white or very bright grey
        if item[0] > 220 and item[1] > 220 and item[2] > 220:
            # Make it transparent
            newData.append((255, 255, 255, 0))
        else:
            newData.append(item)
            
    img.putdata(newData)
    
    # Save as PNG
    img.save(output_path, "PNG")
    print("Background removed and saved to", output_path)
except Exception as e:
    print("Error removing background:", e)
