import os 
from PIL import Image

def convert_bytes(num):
    """
    this function will convert bytes to MB.... GB... etc
    """
    for x in ['bytes', 'KB', 'MB', 'GB', 'TB']:
        if num < 1024.0:
            return "%3.1f %s" % (num, x)
        num /= 1024.0

dirName = "C:\\!playground\\pillow_playground\\myfolder"
names = os.listdir(dirName)
for name in names:
	fullname = os.path.join(dirName, name) # получаем полное имя
	if os.path.isfile(fullname):
		file_info = os.stat(fullname)
		im = Image.open(fullname)
		print(convert_bytes(file_info.st_size), im.size)