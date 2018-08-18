import matplotlib.pyplot as plt
import pydicom

import matplotlib


matplotlib.use('TkAgg')
# from pydicom.data import get_testdata_files

path = 'images/test0.dcm'
# filename = get_testdata_files(path)[0]
ds = pydicom.dcmread(path)
plt.imshow(ds.pixel_array, cmap=plt.cm.bone)
plt.show()
