
from __future__ import print_function
from PIL import Image
import SimpleITK as sitk

fixed_image = '../images/fixedImage.png'
fixed = sitk.ReadImage(fixed_image, sitk.sitkFloat64)

image = sitk.Image(256, 128, 64, sitk.sitkInt16)
image_2D = sitk.Image(64, 64, sitk.sitkFloat32)
image_RGB = sitk.Image([128,128], sitk.sitkVectorUInt8, 3)

nda = sitk.GetArrayViewFromImage(fixed)
my_pil = Image.fromarray(nda)
my_pil.show()
print(nda)


