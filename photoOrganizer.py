import os
from datetime import datetime
from PIL import Image
import PIL.ExifTags
import shutil

#Function Format the Date by the way we need 
def folderPath (file):
    date = photoShootDate(file)
    return date.strftime('%Y') + '/' + date.strftime('%Y-%m-%d')

#Function to Catch the Date of the File 
def photoShootDate(file):
    photo = Image.open(file)
    inf = photo.getdata()
    if 36867 in inf:
        date = inf[36867]
        date = datetime.strptime(date, '%Y:%m:%d %H:%M:%S')
    else:
        date = datetime.fromtimestamp(os.path.getmtime(file))
    return date

#Function to move the photo

def moveFiles(file): 
    newFolder = folderPath(file)
    if not os.path.exists(newFolder):
        os.makedirs(newFolder)
    shutil.move(file, newFolder + '/' + file)



moveFiles('test.jpg')
