from PIL import Image

im = Image.open("media.png")
for i in range(10, 101, 10):
	im = im.convert('RGB')
	im.save(str(i) + "_compress.jpg", optimize=True, quality=i)