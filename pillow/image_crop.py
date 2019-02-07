from PIL import Image, ImageOps
import os, sys

size = (900, 900)


for infile in sys.argv[1:]:
	modes = [
		Image.NEAREST
	]
	for mode in modes:
		outfile = os.path.splitext(infile)[0] + "_" + str(mode) + ".jpeg"
		try:
		    im = Image.open(infile)
		    max_size = min((im.width, im.height))
		    im = ImageOps.fit(im, (max_size, max_size), mode)
		    #im = Image.open("temp.jpeg")
		    im = im.resize(size)
		    im.save(outfile, "JPEG")
		except IOError:
		    print("cannot create crop image for", infile)