#!/usr/local/bin/python3
from PIL import Image

# CREATE A PIXELATED VERSIÓN OF A IMAGE.

# Open image file
img = Image.open("image.png")

# Resize smoothly down to 16x16 pixels
imgSmall = img.resize((16,16),resample=Image.BILINEAR)

# Scale back up using NEAREST to original size
result = imgSmall.resize(img.size,Image.NEAREST)

# Save
result.save('result.png')
