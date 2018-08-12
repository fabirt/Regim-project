from __future__ import print_function
from functools import reduce

import SimpleITK as sitk
from PIL import Image
import sys
import os


def command_iteration(method) :
    if method.GetOptimizerIteration() == 0:
        print("Estimated Scales: ", method.GetOptimizerScales())
    print("{0:3} = {1:7.5f} : {2}".format(
        method.GetOptimizerIteration(),
        method.GetMetricValue(),
        method.GetOptimizerPosition())
    )


pixelType = sitk.sitkFloat32

fixed_file = '../images/fixedImage.png'
moving_file = '../images/movingImage.png'

fixed = sitk.ReadImage(fixed_file, sitk.sitkFloat32)

moving = sitk.ReadImage(moving_file, sitk.sitkFloat32)

R = sitk.ImageRegistrationMethod()

R.SetMetricAsCorrelation()

R.SetOptimizerAsRegularStepGradientDescent(learningRate=2.0,
                                           minStep=1e-4,
                                           numberOfIterations=500,
                                           gradientMagnitudeTolerance=1e-8)
R.SetOptimizerScalesFromIndexShift()

tx = sitk.CenteredTransformInitializer(fixed, moving, sitk.Similarity2DTransform())
R.SetInitialTransform(tx)

R.SetInterpolator(sitk.sitkLinear)

R.AddCommand(sitk.sitkIterationEvent, lambda: command_iteration(R))

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
    resampler.SetDefaultPixelValue(1)
    resampler.SetTransform(outTx)

    out = resampler.Execute(moving)

    simg1 = sitk.Cast(sitk.RescaleIntensity(fixed), sitk.sitkUInt8)
    simg2 = sitk.Cast(sitk.RescaleIntensity(out), sitk.sitkUInt8)
    cimg = sitk.Compose(simg1, simg2, simg1//2.+simg2//2.)

    nda = sitk.GetArrayViewFromImage(cimg)
    my_pil = Image.fromarray(nda)
    my_pil.show()

    # sitk.Show(cimg, "ImageRegistration2 Composition")
