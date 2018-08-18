import Imreg.RegistrationMethods as Reg

GROUP = 'K'
FIXED_IMAGE = 'Data/Method3/'+GROUP+'/input_1.png'
MOVING_IMAGE = 'Data/Method3/'+GROUP+'/input_2.png'

my_imreg = Reg.Imreg(FIXED_IMAGE, MOVING_IMAGE)

result = my_imreg.image_registration_method_bspline2()

print(my_imreg.info_data)
