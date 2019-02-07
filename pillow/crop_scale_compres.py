# 1. Проверка на расширение файла jpeg, jpg, png                    check
# 2. Проверка картинки на валидность im.verify                      check
# 3. Перевод картинки в RGB                                         check            
# 4. Белые рамки сверху или снизу, чтобы картинка стала квадратной  check
# 5. Сжимаем до 900х900                                             check
# 6. Сохраняем с качеством 80 и расширением JPEG                    check
# 7. Стоит ли проверять хэдеры?
import os
from PIL import Image, ImageOps


valide_headers = ['jpeg', 'png']
valide_extensions = ['jpeg', 'png', 'jpg']

def crop_scale_compress(image):
    img = Image.open(image)
    # img.verify()

    img = img.convert('RGB')
    
    max_size = max((img.width, img.height))
    old_size = img.size

    new_size = (max_size, max_size)
    new_im = Image.new("RGB", new_size, color=(255, 255, 255))  
    new_im.paste(img, ((new_size[0]-old_size[0])//2,
                        (new_size[1]-old_size[1])//2))

    img = ImageOps.fit(new_im, (900, 900), centering=(0.5, 0.5))
    return img

folder = "test"    

# Берутся все картинки из папки test
current_dir = os.getcwd() 					# Текущая папка
dirName = os.path.join(current_dir, folder)	# Папка с изображениями
names = os.listdir(dirName)

try:
	os.mkdir("test_out")						# Папка с обработанными изображениями
except Exception:
	pass

for name in names:
    image_name = name.split('.')
    if len(image_name) >= 2:
        image_extension = image_name[-1].lower()
        if image_extension not in valide_extensions:
            print ("Incorrect file extention. Pass jpeg or png image. File: " + name)
            continue
    else:
        print ("The image doesn't have an extention. File: " + name)
        continue

    try:
        im = crop_scale_compress(folder+ "\\"+name)
    except Exception as e:
        print("Invalid file: " + name)
        print(str(e))
        continue

    out_name = image_name[0] + ".jpeg"
    im.save("test_out\\"+ out_name, format='JPEG', optimization=True, quality=80)