import os
from datetime import datetime
from PIL import Image
import PIL.ExifTags
import shutil

#Global Variables

extensions = ['jpg', 'jpeg', 'JPG', 'JPEG']


class PhotoOrganize:

    #Function Format the Date by the way we need 
    def folderPath (self, file):
        date = photoShootDate(file)
        return date.strftime('%Y') + '/' + date.strftime('%Y-%m-%d')

    #Function to Catch the Date of the File 
    def photoShootDate(self,file):
        photo = Image.open(file)
        inf = photo.getdata()
        if 36867 in inf:
            date = inf[36867]
            date = datetime.strptime(date, '%Y:%m:%d %H:%M:%S')
        else:
            date = datetime.fromtimestamp(os.path.getmtime(file))
        return date

    #Function to move the photo

    def moveFiles(self,file): 
        newFolder = folderPath(file)
        if not os.path.exists(newFolder):
            os.makedirs(newFolder)
        shutil.move(file, newFolder + '/' + file)

    #Functio to catch all the photos

    def organize(self): 
        global extensions
        photos =  [
            filename for filename in os.listdir('.') if any(filename.endswith(ext) for ext in extensions)
        ] 

        for filename in photos:
            moveFiles(filename)

    #Test Area

    print(organize())