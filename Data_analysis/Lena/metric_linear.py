from Imreg import RegistrationMethods as Reg
import os

METRIC = "MI"
fixed_path = "lena_fixed.jpg"
path_list = ["lena1.jpg", "lena2.jpg", "lena3.jpg", "lena4.jpg", "lena5.jpg"]
metric_list = [0.0]*len(path_list)
counter = 0
print("Running...")

NEW_DIRECTORY = './output/' + METRIC
if not os.path.exists(NEW_DIRECTORY):
    os.makedirs(NEW_DIRECTORY)

for moving_path in path_list:
    regim_instance = Reg.Imreg(fixed_path, moving_path)
    registered = regim_instance.image_registration_method_displacement()
    registered.save(NEW_DIRECTORY + '/output{0}.png'.format(counter+1))
    info_data = regim_instance.info_data.split(" Metric value:" + "\n")[1]
    metric_list[counter] = float(info_data)
    print("Metric value: {0}".format(metric_list[counter]))
    print(" Process {0} complete ------------------------------------------".format(counter))
    counter += 1
dic = {METRIC: metric_list}
print(dic)
