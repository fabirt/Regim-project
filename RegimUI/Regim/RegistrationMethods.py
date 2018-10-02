
# -----------------------------------------------------------------------------
# IMPORTS
# -----------------------------------------------------------------------------
import SimpleITK as Sitk
from PIL import Image
from math import pi
import os


class Imreg:

    def __init__(self, fixed_path, moving_path):
        """This class have a series of image registration methods"""
        self.fixed_path = fixed_path
        self.moving_path = moving_path
        self.info_data = None

    def demons_registration(self):
        try:
            fixed = Sitk.ReadImage(self.fixed_path)

            moving = Sitk.ReadImage(self.moving_path)

            matcher = Sitk.HistogramMatchingImageFilter()
            matcher.SetNumberOfHistogramLevels(1024)
            matcher.SetNumberOfMatchPoints(7)
            matcher.ThresholdAtMeanIntensityOn()
            moving = matcher.Execute(moving, fixed)

            # The basic Demons Registration Filter
            # Note there is a whole family of Demons Registration algorithms included in SimpleITK
            demons = Sitk.DemonsRegistrationFilter()
            demons.SetNumberOfIterations(50)
            # Standard deviation for Gaussian smoothing of displacement field
            demons.SetStandardDeviations(1.0)

            displacementField = demons.Execute(fixed, moving)

            outTx = Sitk.DisplacementFieldTransform(displacementField)

            if not "SITK_NOSHOW" in os.environ:
                resampler = Sitk.ResampleImageFilter()
                resampler.SetReferenceImage(fixed)
                resampler.SetInterpolator(Sitk.sitkLinear)
                resampler.SetDefaultPixelValue(100)
                resampler.SetTransform(outTx)

                out = resampler.Execute(moving)
                simg1 = Sitk.Cast(Sitk.RescaleIntensity(fixed), Sitk.sitkUInt8)
                simg2 = Sitk.Cast(Sitk.RescaleIntensity(out), Sitk.sitkUInt8)
                # Use the // floor division operator so that the pixel type is
                # the same for all three images which is the expectation for
                # the compose filter.
                cimg = Sitk.Compose(simg1, simg2, simg1 // 2. + simg2 // 2.)

                nda = Sitk.GetArrayViewFromImage(cimg)
                my_image = Image.fromarray(nda)

                return my_image
        except:
            pass

    def demons_registration2(self):
        try:
            fixed = Sitk.ReadImage(self.fixed_path)

            moving = Sitk.ReadImage(self.moving_path)

            matcher = Sitk.HistogramMatchingImageFilter()
            if fixed.GetPixelID() in (Sitk.sitkUInt8, Sitk.sitkInt8):
                matcher.SetNumberOfHistogramLevels(128)
            else:
                matcher.SetNumberOfHistogramLevels(1024)
            matcher.SetNumberOfMatchPoints(7)
            matcher.ThresholdAtMeanIntensityOn()
            moving = matcher.Execute(moving, fixed)

            # The fast symmetric forces Demons Registration Filter
            # Note there is a whole family of Demons Registration algorithms included in SimpleITK
            demons = Sitk.FastSymmetricForcesDemonsRegistrationFilter()
            demons.SetNumberOfIterations(200)
            # Standard deviation for Gaussian smoothing of displacement field
            demons.SetStandardDeviations(1.0)

            displacementField = demons.Execute(fixed, moving)

            outTx = Sitk.DisplacementFieldTransform(displacementField)

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

                return my_image
        except:
            pass

    def image_registration_method1(self):
        try:
            fixed = Sitk.ReadImage(self.fixed_path, Sitk.sitkFloat32)

            moving = Sitk.ReadImage(self.moving_path, Sitk.sitkFloat32)

            R = Sitk.ImageRegistrationMethod()
            R.SetMetricAsMeanSquares()
            R.SetOptimizerAsRegularStepGradientDescent(4.0, .01, 200)
            R.SetInitialTransform(Sitk.TranslationTransform(fixed.GetDimension()))
            R.SetInterpolator(Sitk.sitkLinear)

            outTx = R.Execute(fixed, moving)

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

                return my_image
        except:
            pass

    def image_registration_method2(self):
        try:
            fixed = Sitk.ReadImage(self.fixed_path, Sitk.sitkFloat32)
            fixed = Sitk.Normalize(fixed)
            fixed = Sitk.DiscreteGaussian(fixed, 2.0)

            moving = Sitk.ReadImage(self.moving_path, Sitk.sitkFloat32)
            moving = Sitk.Normalize(moving)
            moving = Sitk.DiscreteGaussian(moving, 2.0)

            R = Sitk.ImageRegistrationMethod()

            R.SetMetricAsJointHistogramMutualInformation()

            R.SetOptimizerAsGradientDescentLineSearch(learningRate=1.0,
                                                      numberOfIterations=200,
                                                      convergenceMinimumValue=1e-5,
                                                      convergenceWindowSize=5)

            R.SetInitialTransform(Sitk.TranslationTransform(fixed.GetDimension()))

            R.SetInterpolator(Sitk.sitkLinear)

            outTx = R.Execute(fixed, moving)

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
                return my_image
        except:
            pass

    def image_registration_method3(self, max_iterations):
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

    def image_registration_method_bspline1(self):
        try:

            fixed = Sitk.ReadImage(self.fixed_path, Sitk.sitkFloat32)

            moving = Sitk.ReadImage(self.moving_path, Sitk.sitkFloat32)

            transformDomainMeshSize = [8] * moving.GetDimension()
            tx = Sitk.BSplineTransformInitializer(fixed, transformDomainMeshSize)

            R = Sitk.ImageRegistrationMethod()
            R.SetMetricAsCorrelation()

            R.SetOptimizerAsLBFGSB(gradientConvergenceTolerance=1e-5,
                                   numberOfIterations=100,
                                   maximumNumberOfCorrections=5,
                                   maximumNumberOfFunctionEvaluations=1000,
                                   costFunctionConvergenceFactor=1e+7)
            R.SetInitialTransform(tx, True)
            R.SetInterpolator(Sitk.sitkLinear)

            outTx = R.Execute(fixed, moving)

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

                return my_image
        except:
            pass

    def image_registration_method_bspline2(self):
        try:
            fixed = Sitk.ReadImage(self.fixed_path, Sitk.sitkFloat32)

            moving = Sitk.ReadImage(self.moving_path, Sitk.sitkFloat32)

            transformDomainMeshSize = [10] * moving.GetDimension()
            tx = Sitk.BSplineTransformInitializer(fixed,
                                                  transformDomainMeshSize)

            R = Sitk.ImageRegistrationMethod()
            R.SetMetricAsMattesMutualInformation(50)
            R.SetOptimizerAsGradientDescentLineSearch(5.0, 100,
                                                      convergenceMinimumValue=1e-4,
                                                      convergenceWindowSize=5)
            R.SetOptimizerScalesFromPhysicalShift()
            R.SetInitialTransform(tx)
            R.SetInterpolator(Sitk.sitkLinear)

            R.SetShrinkFactorsPerLevel([6, 2, 1])
            R.SetSmoothingSigmasPerLevel([6, 2, 1])

            outTx = R.Execute(fixed, moving)

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

                return my_image
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

    def image_registration_method_exhaustive(self):
        try:
            fixed = Sitk.ReadImage(self.fixed_path, Sitk.sitkFloat32)

            moving = Sitk.ReadImage(self.moving_path, Sitk.sitkFloat32)

            R = Sitk.ImageRegistrationMethod()

            R.SetMetricAsMattesMutualInformation(numberOfHistogramBins=50)

            sample_per_axis = 50
            tx = None
            if fixed.GetDimension() == 2:
                tx = Sitk.Euler2DTransform()
                # Set the number of samples (radius) in each dimension, with a
                # default step size of 1.0
                R.SetOptimizerAsExhaustive([sample_per_axis // 2, 0, 0])
                # Utilize the scale to set the step size for each dimension
                R.SetOptimizerScales([2.0 * pi / sample_per_axis, 1.0, 1.0])
            elif fixed.GetDimension() == 3:
                tx = Sitk.Euler3DTransform()
                R.SetOptimizerAsExhaustive([sample_per_axis // 2, sample_per_axis // 2, sample_per_axis // 4, 0, 0, 0])
                R.SetOptimizerScales(
                    [2.0 * pi / sample_per_axis, 2.0 * pi / sample_per_axis, 2.0 * pi / sample_per_axis, 1.0, 1.0, 1.0])

            # Initialize the transform with a translation and the center of
            # rotation from the moments of intensity.
            tx = Sitk.CenteredTransformInitializer(fixed, moving, tx)

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

                return my_image
        except:
            pass
