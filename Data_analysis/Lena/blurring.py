import cv2
from numpy import array
from PIL import Image

LENA = "lena.jpg"
file = "lena_fixed.jpg"
SIZE = (300, 300)
img = Image.open(LENA)
bw = img.convert("L")
bw.thumbnail(SIZE, Image.ANTIALIAS)
bw.save(file)
np_im = cv2.imread(file, 1)

SPACING = 3
for i in range(1, 6):
    blur_value = i*SPACING
    blur = cv2.blur(np_im, (blur_value, blur_value))
    cv2.imwrite("lena{0}.jpg".format(i), blur)
