# -*- coding: utf-8 -*-

"""
Get registration metric value for 40 PNG files
"""

import os
import Imreg.RegistrationMethods as Reg

selector = True
if selector is False:
    METHOD = "Mutual information"
else:
    METHOD = "Mean squares"

png_dir = "./png_files"

fixed_list = list(range(1, 41, 2))
moving_list = list(range(2, 41, 2))
metric_list = list(range(1, 41, 2))

counter = 1

print(METHOD)
for item in fixed_list:
    fixed_path = "{0}/{1}.png".format(png_dir, item)
    moving_path = "{0}/{1}.png".format(png_dir, item + 1)
    regim = Reg.Imreg(fixed_path, moving_path)
    img = regim.image_registration_method_displacement()
    info_data = regim.info_data.split(" Metric value:" + "\n")[1]
    metric_list[counter-1] = float(info_data)
    print(fixed_path + " : " + moving_path)
    print("Restantes: {0}".format(20-counter))
    print(info_data)
    counter += 1
print(metric_list)
