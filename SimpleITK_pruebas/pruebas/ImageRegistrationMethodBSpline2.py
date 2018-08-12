from __future__ import print_function

import SimpleITK as sitk
from PIL import Image
import sys
import os


def command_iteration(method):
    print("{0:3} = {1:10.5f}".format(method.GetOptimizerIteration(),
                                     method.GetMetricValue()))
    print("\t#: ", len(method.GetOptimizerPosition()))


def command_multi_iteration(method):
    print("--------- Resolution Changing ---------")


fixed_file = '../images/fixedImage.png'
moving_file = '../images/movingImage.png'

fixed = sitk.ReadImage(fixed_file, sitk.sitkFloat32)

moving = sitk.ReadImage(moving_file, sitk.sitkFloat32)

transformDomainMeshSize = [10]*moving.GetDimension()
tx = sitk.BSplineTransformInitializer(fixed,
                                      transformDomainMeshSize)

print("Initial Parameters:")
print(tx.GetParameters())

R = sitk.ImageRegistrationMethod()
R.SetMetricAsMattesMutualInformation(50)
R.SetOptimizerAsGradientDescentLineSearch(5.0, 100,
                                          convergenceMinimumValue=1e-4,
                                          convergenceWindowSize=5)
R.SetOptimizerScalesFromPhysicalShift()
R.SetInitialTransform(tx)
R.SetInterpolator(sitk.sitkLinear)

R.SetShrinkFactorsPerLevel([6, 2, 1])
R.SetSmoothingSigmasPerLevel([6, 2, 1])

R.AddCommand(sitk.sitkIterationEvent, lambda: command_iteration(R))
R.AddCommand(sitk.sitkMultiResolutionIterationEvent, lambda: command_multi_iteration(R))

outTx = R.Execute(fixed, moving)

print("-------")
print(outTx)
print("Optimizer stop condition: {0}".format(R.GetOptimizerStopConditionDescription()))
print(" Iteration: {0}".format(R.GetOptimizerIteration()))
print(" Metric value: {0}".format(R.GetMetricValue()))

# sitk.WriteTransform(outTx,  sys.argv[3])

if not "SITK_NOSHOW" in os.environ:

    resampler = sitk.ResampleImageFilter()
    resampler.SetReferenceImage(fixed)
    resampler.SetInterpolator(sitk.sitkLinear)
    resampler.SetDefaultPixelValue(100)
    resampler.SetTransform(outTx)

    out = resampler.Execute(moving)
    simg1 = sitk.Cast(sitk.RescaleIntensity(fixed), sitk.sitkUInt8)
    simg2 = sitk.Cast(sitk.RescaleIntensity(out), sitk.sitkUInt8)
    cimg = sitk.Compose(simg1, simg2, simg1//2.+simg2//2.)

    nda = sitk.GetArrayViewFromImage(cimg)
    my_pil = Image.fromarray(nda)
    my_pil.show()

    # sitk.Show(cimg, "ImageRegistration1 Composition")
