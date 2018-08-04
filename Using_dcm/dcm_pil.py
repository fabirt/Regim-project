import pydicom
from PIL import Image


Ima = pydicom.dcmread("images/test0.dcm")  # change the path

# I just had to print this Ima.pixel_array out to show you the lists
f = Ima.pixel_array

sa = Image.fromarray(f)  # Hear is the Image module. It needs the array method as the details from Ima. is array
sa.show()
