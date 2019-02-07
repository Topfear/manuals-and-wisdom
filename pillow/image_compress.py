import os 
from PIL import Image, ImageOps

try:
	os.mkdir("myfolder")
except:
	pass

dirName = "C:\\!playground\\pillow_playground\\new_wallpaper"
names = os.listdir(dirName)
for name in names:
	fullname = os.path.join(dirName, name) # получаем полное имя
	if os.path.isfile(fullname):
		outfile = os.path.splitext(name)[0] + ".jpeg"
		try:
			im = Image.open("new_wallpaper\\"+name)
			im = im.convert('RGB')
			max_size = min((im.width, im.height))
			im = ImageOps.fit(im, (max_size, max_size))
			im = im.resize((900, 900))
			im.save(
				"myfolder\\"+ outfile, 
				optimization=True, 
				quality=50
			)
		except:
			pass