from PIL import Image
from PIL.ExifTags import TAGS

while True:
    imagename = input("Image: ")
    image = Image.open(imagename)
    exifdata = image._getexif()
    if exifdata is not None:
	for tag_id in exifdata:
		tag = TAGS.get(tag_id, tag_id)
		data = exifdata.get(tag_id)
                if isinstance(data, bytes):
		    data = data.decode()
                print('{} {}'.format(tag,data))
    else:
	print("NO DATA")
