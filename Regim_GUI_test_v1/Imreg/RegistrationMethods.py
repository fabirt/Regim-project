
# -----------------------------------------------------------------------------
# IMPORTS
# -----------------------------------------------------------------------------
import SimpleITK as sitk
from PIL import Image
from math import pi
import sys
import os


class Imreg:

    def __init__(self, fixed_path, moving_path):
        self.fixed_path = fixed_path
        self.moving_path = moving_path

    def demons_registration(self):
        try:
            fixed = sitk.ReadImage(self.fixed_path)

            moving = sitk.ReadImage(self.moving_path)

            matcher = sitk.HistogramMatchingImageFilter()
            matcher.SetNumberOfHistogramLevels(1024)
            matcher.SetNumberOfMatchPoints(7)
            matcher.ThresholdAtMeanIntensityOn()
            moving = matcher.Execute(moving, fixed)

            # The basic Demons Registration Filter
            # Note there is a whole family of Demons Registration algorithms included in SimpleITK
            demons = sitk.DemonsRegistrationFilter()
            demons.SetNumberOfIterations(50)
            # Standard deviation for Gaussian smoothing of displacement field
            demons.SetStandardDeviations(1.0)

            displacementField = demons.Execute(fixed, moving)

            outTx = sitk.DisplacementFieldTransform(displacementField)

            if not "SITK_NOSHOW" in os.environ:
                resampler = sitk.ResampleImageFilter()
                resampler.SetReferenceImage(fixed)
                resampler.SetInterpolator(sitk.sitkLinear)
                resampler.SetDefaultPixelValue(100)
                resampler.SetTransform(outTx)

                out = resampler.Execute(moving)
                simg1 = sitk.Cast(sitk.RescaleIntensity(fixed), sitk.sitkUInt8)
                simg2 = sitk.Cast(sitk.RescaleIntensity(out), sitk.sitkUInt8)
                # Use the // floor division operator so that the pixel type is
                # the same for all three images which is the expectation for
                # the compose filter.
                cimg = sitk.Compose(simg1, simg2, simg1 // 2. + simg2 // 2.)

                nda = sitk.GetArrayViewFromImage(cimg)
                my_image = Image.fromarray(nda)

                return my_image
        except:
            pass

    def demons_registration2(self):
        try:
            fixed = sitk.ReadImage(self.fixed_path)

            moving = sitk.ReadImage(self.moving_path)

            matcher = sitk.HistogramMatchingImageFilter()
            if fixed.GetPixelID() in (sitk.sitkUInt8, sitk.sitkInt8):
                matcher.SetNumberOfHistogramLevels(128)
            else:
                matcher.SetNumberOfHistogramLevels(1024)
            matcher.SetNumberOfMatchPoints(7)
            matcher.ThresholdAtMeanIntensityOn()
            moving = matcher.Execute(moving, fixed)

            # The fast symmetric forces Demons Registration Filter
            # Note there is a whole family of Demons Registration algorithms included in SimpleITK
            demons = sitk.FastSymmetricForcesDemonsRegistrationFilter()
            demons.SetNumberOfIterations(200)
            # Standard deviation for Gaussian smoothing of displacement field
            demons.SetStandardDeviations(1.0)

            displacementField = demons.Execute(fixed, moving)

            outTx = sitk.DisplacementFieldTransform(displacementField)

            if not "SITK_NOSHOW" in os.environ:
                resampler = sitk.ResampleImageFilter()
                resampler.SetReferenceImage(fixed)
                resampler.SetInterpolator(sitk.sitkLinear)
                resampler.SetDefaultPixelValue(100)
                resampler.SetTransform(outTx)

                out = resampler.Execute(moving)
                simg1 = sitk.Cast(sitk.RescaleIntensity(fixed), sitk.sitkUInt8)
                simg2 = sitk.Cast(sitk.RescaleIntensity(out), sitk.sitkUInt8)
                cimg = sitk.Compose(simg1, simg2, simg1 // 2. + simg2 // 2.)

                nda = sitk.GetArrayViewFromImage(cimg)
                my_image = Image.fromarray(nda)

                return my_image
        except:
            pass

    def image_registration_method1(self):
        try:
            fixed = sitk.ReadImage(self.fixed_path, sitk.sitkFloat32)

            moving = sitk.ReadImage(self.moving_path, sitk.sitkFloat32)

            R = sitk.ImageRegistrationMethod()
            R.SetMetricAsMeanSquares()
            R.SetOptimizerAsRegularStepGradientDescent(4.0, .01, 200)
            R.SetInitialTransform(sitk.TranslationTransform(fixed.GetDimension()))
            R.SetInterpolator(sitk.sitkLinear)

            outTx = R.Execute(fixed, moving)

            if not "SITK_NOSHOW" in os.environ:
                resampler = sitk.ResampleImageFilter()
                resampler.SetReferenceImage(fixed)
                resampler.SetInterpolator(sitk.sitkLinear)
                resampler.SetDefaultPixelValue(100)
                resampler.SetTransform(outTx)

                out = resampler.Execute(moving)
                simg1 = sitk.Cast(sitk.RescaleIntensity(fixed), sitk.sitkUInt8)
                simg2 = sitk.Cast(sitk.RescaleIntensity(out), sitk.sitkUInt8)
                cimg = sitk.Compose(simg1, simg2, simg1 // 2. + simg2 // 2.)

                nda = sitk.GetArrayViewFromImage(cimg)
                my_image = Image.fromarray(nda)

                return my_image
        except:
            pass


    def image_registration_method2(self):
        try:
            fixed = sitk.ReadImage(self.fixed_path, sitk.sitkFloat32)
            fixed = sitk.Normalize(fixed)
            fixed = sitk.DiscreteGaussian(fixed, 2.0)

            moving = sitk.ReadImage(self.moving_path, sitk.sitkFloat32)
            moving = sitk.Normalize(moving)
            moving = sitk.DiscreteGaussian(moving, 2.0)

            R = sitk.ImageRegistrationMethod()

            R.SetMetricAsJointHistogramMutualInformation()

            R.SetOptimizerAsGradientDescentLineSearch(learningRate=1.0,
                                                      numberOfIterations=200,
                                                      convergenceMinimumValue=1e-5,
                                                      convergenceWindowSize=5)

            R.SetInitialTransform(sitk.TranslationTransform(fixed.GetDimension()))

            R.SetInterpolator(sitk.sitkLinear)

            outTx = R.Execute(fixed, moving)

            if not "SITK_NOSHOW" in os.environ:
                resampler = sitk.ResampleImageFilter()
                resampler.SetReferenceImage(fixed)
                resampler.SetInterpolator(sitk.sitkLinear)
                resampler.SetDefaultPixelValue(1)
                resampler.SetTransform(outTx)

                out = resampler.Execute(moving)

                simg1 = sitk.Cast(sitk.RescaleIntensity(fixed), sitk.sitkUInt8)
                simg2 = sitk.Cast(sitk.RescaleIntensity(out), sitk.sitkUInt8)
                cimg = sitk.Compose(simg1, simg2, simg1 // 2. + simg2 // 2.)

                nda = sitk.GetArrayViewFromImage(cimg)
                my_image = Image.fromarray(nda)
                return my_image
        except:
            pass


    def image_registration_method3(self):
        try:
            fixed = sitk.ReadImage(self.fixed_path, sitk.sitkFloat32)

            moving = sitk.ReadImage(self.moving_path, sitk.sitkFloat32)

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

            outTx = R.Execute(fixed, moving)

            if not "SITK_NOSHOW" in os.environ:
                resampler = sitk.ResampleImageFilter()
                resampler.SetReferenceImage(fixed)
                resampler.SetInterpolator(sitk.sitkLinear)
                resampler.SetDefaultPixelValue(1)
                resampler.SetTransform(outTx)

                out = resampler.Execute(moving)

                simg1 = sitk.Cast(sitk.RescaleIntensity(fixed), sitk.sitkUInt8)
                simg2 = sitk.Cast(sitk.RescaleIntensity(out), sitk.sitkUInt8)
                cimg = sitk.Compose(simg1, simg2, simg1 // 2. + simg2 // 2.)

                nda = sitk.GetArrayViewFromImage(cimg)
                my_image = Image.fromarray(nda)

                return my_image
        except:
            pass

    def image_registration_method_bspline1(self):
        try:

            fixed = sitk.ReadImage(self.fixed_path, sitk.sitkFloat32)

            moving = sitk.ReadImage(self.moving_path, sitk.sitkFloat32)

            transformDomainMeshSize = [8] * moving.GetDimension()
            tx = sitk.BSplineTransformInitializer(fixed, transformDomainMeshSize)

            R = sitk.ImageRegistrationMethod()
            R.SetMetricAsCorrelation()

            R.SetOptimizerAsLBFGSB(gradientConvergenceTolerance=1e-5,
                                   numberOfIterations=100,
                                   maximumNumberOfCorrections=5,
                                   maximumNumberOfFunctionEvaluations=1000,
                                   costFunctionConvergenceFactor=1e+7)
            R.SetInitialTransform(tx, True)
            R.SetInterpolator(sitk.sitkLinear)

            outTx = R.Execute(fixed, moving)

            if not "SITK_NOSHOW" in os.environ:
                resampler = sitk.ResampleImageFilter()
                resampler.SetReferenceImage(fixed)
                resampler.SetInterpolator(sitk.sitkLinear)
                resampler.SetDefaultPixelValue(100)
                resampler.SetTransform(outTx)

                out = resampler.Execute(moving)
                simg1 = sitk.Cast(sitk.RescaleIntensity(fixed), sitk.sitkUInt8)
                simg2 = sitk.Cast(sitk.RescaleIntensity(out), sitk.sitkUInt8)
                cimg = sitk.Compose(simg1, simg2, simg1 // 2. + simg2 // 2.)

                nda = sitk.GetArrayViewFromImage(cimg)
                my_image = Image.fromarray(nda)

                return my_image
        except:
            pass

    def image_registration_method_bspline2(self):
        try:
            fixed = sitk.ReadImage(self.fixed_path, sitk.sitkFloat32)

            moving = sitk.ReadImage(self.moving_path, sitk.sitkFloat32)

            transformDomainMeshSize = [10] * moving.GetDimension()
            tx = sitk.BSplineTransformInitializer(fixed,
                                                  transformDomainMeshSize)

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

            outTx = R.Execute(fixed, moving)

            if not "SITK_NOSHOW" in os.environ:
                resampler = sitk.ResampleImageFilter()
                resampler.SetReferenceImage(fixed)
                resampler.SetInterpolator(sitk.sitkLinear)
                resampler.SetDefaultPixelValue(100)
                resampler.SetTransform(outTx)

                out = resampler.Execute(moving)
                simg1 = sitk.Cast(sitk.RescaleIntensity(fixed), sitk.sitkUInt8)
                simg2 = sitk.Cast(sitk.RescaleIntensity(out), sitk.sitkUInt8)
                cimg = sitk.Compose(simg1, simg2, simg1 // 2. + simg2 // 2.)

                nda = sitk.GetArrayViewFromImage(cimg)
                my_image = Image.fromarray(nda)

                return my_image
        except:
            pass

    def image_registration_method_displacement(self):
        try:
            fixed = sitk.ReadImage(self.fixed_path, sitk.sitkFloat32)

            moving = sitk.ReadImage(self.moving_path, sitk.sitkFloat32)

            initialTx = sitk.CenteredTransformInitializer(fixed, moving, sitk.AffineTransform(fixed.GetDimension()))

            R = sitk.ImageRegistrationMethod()

            R.SetShrinkFactorsPerLevel([3, 2, 1])
            R.SetSmoothingSigmasPerLevel([2, 1, 1])

            R.SetMetricAsJointHistogramMutualInformation(20)
            R.MetricUseFixedImageGradientFilterOff()

            R.SetOptimizerAsGradientDescent(learningRate=1.0,
                                            numberOfIterations=100,
                                            estimateLearningRate=R.EachIteration)
            R.SetOptimizerScalesFromPhysicalShift()

            R.SetInitialTransform(initialTx, inPlace=True)

            R.SetInterpolator(sitk.sitkLinear)

            outTx = R.Execute(fixed, moving)

            displacementField = sitk.Image(fixed.GetSize(), sitk.sitkVectorFloat64)
            displacementField.CopyInformation(fixed)
            displacementTx = sitk.DisplacementFieldTransform(displacementField)
            del displacementField
            displacementTx.SetSmoothingGaussianOnUpdate(varianceForUpdateField=0.0,
                                                        varianceForTotalField=1.5)

            R.SetMovingInitialTransform(outTx)
            R.SetInitialTransform(displacementTx, inPlace=True)

            R.SetMetricAsANTSNeighborhoodCorrelation(4)
            R.MetricUseFixedImageGradientFilterOff()

            R.SetShrinkFactorsPerLevel([3, 2, 1])
            R.SetSmoothingSigmasPerLevel([2, 1, 1])

            R.SetOptimizerScalesFromPhysicalShift()
            R.SetOptimizerAsGradientDescent(learningRate=1,
                                            numberOfIterations=300,
                                            estimateLearningRate=R.EachIteration)

            outTx.AddTransform(R.Execute(fixed, moving))

            if not "SITK_NOSHOW" in os.environ:

                resampler = sitk.ResampleImageFilter()
                resampler.SetReferenceImage(fixed)
                resampler.SetInterpolator(sitk.sitkLinear)
                resampler.SetDefaultPixelValue(100)
                resampler.SetTransform(outTx)

                out = resampler.Execute(moving)
                simg1 = sitk.Cast(sitk.RescaleIntensity(fixed), sitk.sitkUInt8)
                simg2 = sitk.Cast(sitk.RescaleIntensity(out), sitk.sitkUInt8)
                cimg = sitk.Compose(simg1, simg2, simg1 // 2. + simg2 // 2.)

                nda = sitk.GetArrayViewFromImage(cimg)
                my_image = Image.fromarray(nda)
                return my_image
        except:
            pass

    def image_registration_method_exhaustive(self):
        try:
            fixed = sitk.ReadImage(self.fixed_path, sitk.sitkFloat32)

            moving = sitk.ReadImage(self.moving_path, sitk.sitkFloat32)

            R = sitk.ImageRegistrationMethod()

            R.SetMetricAsMattesMutualInformation(numberOfHistogramBins=50)

            sample_per_axis = 50
            tx = None
            if fixed.GetDimension() == 2:
                tx = sitk.Euler2DTransform()
                # Set the number of samples (radius) in each dimension, with a
                # default step size of 1.0
                R.SetOptimizerAsExhaustive([sample_per_axis // 2, 0, 0])
                # Utilize the scale to set the step size for each dimension
                R.SetOptimizerScales([2.0 * pi / sample_per_axis, 1.0, 1.0])
            elif fixed.GetDimension() == 3:
                tx = sitk.Euler3DTransform()
                R.SetOptimizerAsExhaustive([sample_per_axis // 2, sample_per_axis // 2, sample_per_axis // 4, 0, 0, 0])
                R.SetOptimizerScales(
                    [2.0 * pi / sample_per_axis, 2.0 * pi / sample_per_axis, 2.0 * pi / sample_per_axis, 1.0, 1.0, 1.0])

            # Initialize the transform with a translation and the center of
            # rotation from the moments of intensity.
            tx = sitk.CenteredTransformInitializer(fixed, moving, tx)

            R.SetInitialTransform(tx)

            R.SetInterpolator(sitk.sitkLinear)

            outTx = R.Execute(fixed, moving)

            if not "SITK_NOSHOW" in os.environ:
                resampler = sitk.ResampleImageFilter()
                resampler.SetReferenceImage(fixed)
                resampler.SetInterpolator(sitk.sitkLinear)
                resampler.SetDefaultPixelValue(1)
                resampler.SetTransform(outTx)

                out = resampler.Execute(moving)

                simg1 = sitk.Cast(sitk.RescaleIntensity(fixed), sitk.sitkUInt8)
                simg2 = sitk.Cast(sitk.RescaleIntensity(out), sitk.sitkUInt8)
                cimg = sitk.Compose(simg1, simg2, simg1 // 2. + simg2 // 2.)

                nda = sitk.GetArrayViewFromImage(cimg)
                my_image = Image.fromarray(nda)

                return my_image
        except:
            pass
