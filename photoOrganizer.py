import os
from datetime import datetime
from PIL import Image
import PIL.ExifTags

# Crating a Function to Catch the Data of thXe Photos


def photoShootDate(file):
    photo = Image.open(file)
    inf = photo.getdata()
    if 36867 in inf:
        date = inf[36867]
        date = datetime.strptime(date, '%Y:%m:%d %H:%M:%S')
    else:
        date = datetime.fromtimestamp(os.path.getmtime(file))
    return date


print(photoShootDate('test.jpg'))
