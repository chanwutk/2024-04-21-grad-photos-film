import os
from PIL import Image

for f in os.listdir():
    if f.endswith(".JPG"):
        img = Image.open(f)
        height, width = img.size
        if width < height:
            img = img.rotate(90, expand=True)
        img.thumbnail((512, 512))
        img.save(f"SMALL-{f}")