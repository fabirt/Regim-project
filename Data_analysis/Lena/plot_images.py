import matplotlib.pyplot as plt
from PIL import Image

selector = 4

moving_inputs = ["lena1.jpg", "lena2.jpg", "lena3.jpg", "lena4.jpg", "lena5.jpg"]
co_outputs = ["./output/CO/output1.png", "./output/CO/output2.png", "./output/CO/output3.png", "./output/CO/output4.png", "./output/CO/output5.png"]
mse_outputs = ["./output/MS/output1.png", "./output/MS/output2.png", "./output/MS/output3.png", "./output/MS/output4.png", "./output/MS/output5.png"]
mi_outputs = ["./output/MI/output1.png", "./output/MI/output2.png", "./output/MI/output3.png", "./output/MI/output4.png", "./output/MI/output5.png"]

if selector == 1:
    images = moving_inputs
elif selector == 2:
    images = co_outputs
elif selector == 3:
    images = mse_outputs
else:
    images = mi_outputs

fixed = Image.open("lena_fixed.jpg")
mov1 = Image.open(images[0])
mov2 = Image.open(images[1])
mov3 = Image.open(images[2])
mov4 = Image.open(images[3])
mov5 = Image.open(images[4])

fig = plt.figure()
ax1 = fig.add_subplot(2, 3, 1)
ax1.set_yticklabels([])
ax1.set_xticklabels([])
ax1.imshow(mov1)
ax2 = fig.add_subplot(2, 3, 2)
ax2.set_yticklabels([])
ax2.set_xticklabels([])
ax2.imshow(mov2)
ax3 = fig.add_subplot(2, 3, 3)
ax3.set_yticklabels([])
ax3.set_xticklabels([])
ax3.imshow(mov3)
ax4 = fig.add_subplot(2, 3, 4)
ax4.set_yticklabels([])
ax4.set_xticklabels([])
ax4.imshow(mov4)
ax5 = fig.add_subplot(2, 3, 5)
ax5.set_yticklabels([])
ax5.set_xticklabels([])
ax5.imshow(mov5)
plt.show()
