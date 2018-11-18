#  -*- coding: utf-8 -*-

# -----------------------------------------------------------------------------
# IMPORTS
# -----------------------------------------------------------------------------
import SimpleITK as Sitk
from PIL import Image
import os


class Imreg:

    def __init__(self, fixed_path, moving_path):
        """This class have a series of image registration methods from SimpleITK"""
        self.fixed_path = fixed_path
        self.moving_path = moving_path
        self.info_data = None

    def image_registration_method_restrictive(self, max_iterations):
        try:
            fixed = Sitk.ReadImage(self.fixed_path, Sitk.sitkFloat32)

            moving = Sitk.ReadImage(self.moving_path, Sitk.sitkFloat32)

            R = Sitk.ImageRegistrationMethod()

            R.SetMetricAsMattesMutualInformation(50)

            R.SetOptimizerAsRegularStepGradientDescent(learningRate=2.0,
                                                       minStep=1e-4,
                                                       numberOfIterations=max_iterations,
                                                       gradientMagnitudeTolerance=1e-8)
            R.SetOptimizerScalesFromIndexShift()

            tx = Sitk.CenteredTransformInitializer(fixed, moving, Sitk.Similarity2DTransform())
            R.SetInitialTransform(tx)

            R.SetInterpolator(Sitk.sitkLinear)

            outTx = R.Execute(fixed, moving)

            info_data = " Iteration: {0}".format(R.GetOptimizerIteration()) + "\n" + "\n" + \
                        " Metric value:" + "\n" + format(R.GetMetricValue())[0:6]
            self.info_data = info_data

            if not "SITK_NOSHOW" in os.environ:
                resampler = Sitk.ResampleImageFilter()
                resampler.SetReferenceImage(fixed)
                resampler.SetInterpolator(Sitk.sitkLinear)
                resampler.SetDefaultPixelValue(1)
                resampler.SetTransform(outTx)

                out = resampler.Execute(moving)

                simg1 = Sitk.Cast(Sitk.RescaleIntensity(fixed), Sitk.sitkUInt8)
                simg2 = Sitk.Cast(Sitk.RescaleIntensity(out), Sitk.sitkUInt8)
                cimg = Sitk.Compose(simg1, simg2, simg1 // 2. + simg2 // 2.)

                nda = Sitk.GetArrayViewFromImage(cimg)
                my_image = Image.fromarray(nda)

                return my_image, nda
        except:
            pass

    def image_registration_method_displacement(self, max_iterations):
        try:
            fixed = Sitk.ReadImage(self.fixed_path, Sitk.sitkFloat32)

            moving = Sitk.ReadImage(self.moving_path, Sitk.sitkFloat32)

            initialTx = Sitk.CenteredTransformInitializer(fixed, moving, Sitk.AffineTransform(fixed.GetDimension()))

            R = Sitk.ImageRegistrationMethod()

            R.SetShrinkFactorsPerLevel([3, 2, 1])
            R.SetSmoothingSigmasPerLevel([2, 1, 1])

            R.SetMetricAsMattesMutualInformation(numberOfHistogramBins=50)

            R.MetricUseFixedImageGradientFilterOff()

            R.SetOptimizerAsGradientDescent(learningRate=1.0,
                                            numberOfIterations=max_iterations,
                                            estimateLearningRate=R.EachIteration)
            R.SetOptimizerScalesFromPhysicalShift()

            R.SetInitialTransform(initialTx, inPlace=True)

            R.SetInterpolator(Sitk.sitkLinear)

            outTx = R.Execute(fixed, moving)

            displacementField = Sitk.Image(fixed.GetSize(), Sitk.sitkVectorFloat64)
            displacementField.CopyInformation(fixed)
            displacementTx = Sitk.DisplacementFieldTransform(displacementField)
            del displacementField
            displacementTx.SetSmoothingGaussianOnUpdate(varianceForUpdateField=0.0,
                                                        varianceForTotalField=1.5)

            R.SetMovingInitialTransform(outTx)
            R.SetInitialTransform(displacementTx, inPlace=True)

            R.SetMetricAsMattesMutualInformation(50)

            R.MetricUseFixedImageGradientFilterOff()

            R.SetShrinkFactorsPerLevel([3, 2, 1])
            R.SetSmoothingSigmasPerLevel([2, 1, 1])

            R.SetOptimizerScalesFromPhysicalShift()
            R.SetOptimizerAsGradientDescent(learningRate=1,
                                            numberOfIterations=max_iterations,
                                            estimateLearningRate=R.EachIteration)

            outTx.AddTransform(R.Execute(fixed, moving))

            info_data = " Iteration: {0}".format(R.GetOptimizerIteration()) + "\n" + "\n" + \
                        " Metric value:" + "\n" + format(R.GetMetricValue())[0:6]
            self.info_data = info_data

            if not "SITK_NOSHOW" in os.environ:

                resampler = Sitk.ResampleImageFilter()
                resampler.SetReferenceImage(fixed)
                resampler.SetInterpolator(Sitk.sitkLinear)
                resampler.SetDefaultPixelValue(100)
                resampler.SetTransform(outTx)

                out = resampler.Execute(moving)
                simg1 = Sitk.Cast(Sitk.RescaleIntensity(fixed), Sitk.sitkUInt8)
                simg2 = Sitk.Cast(Sitk.RescaleIntensity(out), Sitk.sitkUInt8)
                cimg = Sitk.Compose(simg1, simg2, simg1 // 2. + simg2 // 2.)

                nda = Sitk.GetArrayViewFromImage(cimg)
                my_image = Image.fromarray(nda)
                return my_image, nda
        except:
            pass
