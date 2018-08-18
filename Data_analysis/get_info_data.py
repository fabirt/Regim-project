import Imreg.RegistrationMethods as Reg

GROUP = 'A'
FIXED_IMAGE = 'Data/Method3/'+GROUP+'/input_1.png'
MOVING_IMAGE = 'Data/Method3/'+GROUP+'/input_2.png'

my_imreg = Reg.Imreg(FIXED_IMAGE, MOVING_IMAGE)
# Select registration method
result = my_imreg.image_registration_method_displacement()

print(my_imreg.info_data)
