from PIL import Image
from os import listdir

cut_pictures = 'd:\HK'
result_path_target = 'd:\HK2'

ims = [Image.open(cut_pictures + '\\' + fn)
       for fn in listdir(cut_pictures)
       if fn.endswith(".jpg")]  # 打开路径下的所有图片
width, height = ims[0].size  # 获取拼接图片的宽和高
print(ims)
result = Image.new(ims[0].mode, (width, height * len(ims)))
for j, im in enumerate(ims):
    result.paste(im, box=(0, j * height))
    print(j)
result.save(result_path_target + '\\' + 'join.jpg')
