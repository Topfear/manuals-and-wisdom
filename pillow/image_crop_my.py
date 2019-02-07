from PIL import Image, ImageOps
import os, sys

# img 1920 1080
# res 900 900
# x0 = imgx/2 - min(x,y)/2
# y0 = imgy/2 - min(x,y)/2



for infile in sys.argv[1:]:
	outfile = os.path.splitext(infile)[0] + "_.jpeg"
	try:
	    im = Image.open(infile)
	    min_size = min((im.width, im.height))
	    x0 = im.width/2 - min_size/2
	    y0 = im.height/2 - min_size/2
	    x1 = x0 + min_size
	    y1 = y0 + min_size
	    im = im.crop((x0, y0, x1, y1))
	    im.save("1_my.jpeg", optimization=True, quality=10)

	    im = im.resize((900,900))
	    im.save("1_my_900_900.jpeg", optimization=True, quality=10)
	except IOError:
	    print("cannot create crop image for", infile)