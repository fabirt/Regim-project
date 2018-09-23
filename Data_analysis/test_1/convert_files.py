# -*- coding: utf-8 -*-

"""
Read .DCM files in a directory, convert each file to .PNG
and save it in another directory
"""

import os
import Imreg.Resources as Res

dcm_dir = "C:/Users/Fabian/Downloads/DESCARGAS FABI/RIDER NEURO MRI/RIDER Neuro MRI-1023805636/" \
          "09-03-1904-BRAINRESEARCH-88413/17-sag 3d gre c-77368"
dest_dir = "./png_files"

counter = 1
for filename in os.listdir(dcm_dir):
    if counter <= 40:
        origin_path = "{0}/{1}".format(dcm_dir, filename)
        dest_path = "{0}/{1}.png".format(dest_dir, counter)
        Res.dicom_to_png(origin_path, dest_path)
        print(dest_path)
        counter += 1
    else:
        break
