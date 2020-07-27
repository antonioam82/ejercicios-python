from PIL import Image
from PIL.ExifTags import TAGS
import os
os.chdir(r'/home/alfmar/Documentos/Antonio')

while True:
	imagename = raw_input("Image: ")
	image = Image.open(imagename)
	exifdata = image._getexif()
	if exifdata is not None:
	        for tag_id in exifdata:
		    # get the tag name, instead of human unreadable tag id
		    tag = TAGS.get(tag_id, tag_id)
		    data = exifdata.get(tag_id)
		    # decode bytes 
		    if isinstance(data, bytes):
			    data = data.decode()
		    print('{} {}'.format(tag,data))
    else:
		print("NO DATA")
