import os 
import sys
from PIL import Image
import imghdr


for infile in sys.argv[1:]:
	print(imghdr.what(infile))