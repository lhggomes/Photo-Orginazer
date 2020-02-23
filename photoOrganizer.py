import os
from datetime import datetime
from PIL import Image

# Crating a Function to Catch the Data of the Photos


def photoShootDate(file):
    photo = Image.open(file)
    inf = photo._getexif()
    if 36867 in inf:
        date = inf[36867]
        date = datetime.strptime(date, '%Y:%m:%d %H:%M:%S')
    else:
        date = datetime.fromtimestamp(os.path.getmtime(file))
    return date


print(photoShootDate('test.jpg'))
