import os 
import sys
from PIL import Image

dirName = "C:\\!playground\\pillow_playground\\myfolder"
names = os.listdir(dirName)
for infile in sys.argv[1:]:
	im = Image.open(infile)
	max_size = max((im.width, im.height))
	old_size = im.size

	new_size = (max_size, max_size)
	new_im = Image.new("RGB", new_size, color=(255, 255, 255))   ## luckily, this is already black!
	new_im.paste(im, ((new_size[0]-old_size[0])//2,
	                      (new_size[1]-old_size[1])//2))

	new_im.show()