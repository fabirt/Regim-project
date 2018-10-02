# -*- coding: utf-8 -*-
"""
Created on Tue Jul 31 20:08:37 2018

@author: Fabian
"""


# -----------------------------------------------------------------------------
# IMPORTS
# -----------------------------------------------------------------------------
# from PIL import Image
import os
import sys
import numpy as np
import png
import pydicom
import cv2


def resource_path(relative_path):
    """Search file with the relative path"""
    try:
        if hasattr(sys, '_MEIPASS'):
            return os.path.join(sys._MEIPASS, relative_path)
        return os.path.join(os.path.abspath("."), relative_path)
    except:
        pass


def opencv_resize(image_path, width=None, height=None, inter=cv2.INTER_CUBIC, mode=0):
    # initialize the dimensions of the cv2_image to be resized and
    # grab the cv2_image size
    dim = None
    cv2_image = cv2.imread(image_path, mode)
    (h, w) = cv2_image.shape[:2]

    # if both the width and height are None, then return the
    # original cv2_image
    if width is None and height is None:
        return cv2_image

    # check to see if the width is None
    if width is None:
        # calculate the ratio of the height and construct the
        # dimensions
        r = height / float(h)
        dim = (int(w * r), height)

    # otherwise, the height is None
    else:
        # calculate the ratio of the width and construct the
        # dimensions
        r = width / float(w)
        dim = (width, int(h * r))

    # resize the cv2_image
    resized = cv2.resize(cv2_image, dim, interpolation=inter)

    # return the resized cv2_image
    return resized


class Convert:

    def __init__(self):
        self.dicom_file_info = None

    def dicom_to_png(self, dicom_file_path, destination):
        """Convert a DICOM file into a PNG file"""
        props = ["PatientName", 'StudyDate', 'Modality', 'StudyDescription']
        try:
            ds = pydicom.dcmread(dicom_file_path)
            # Read DICOM data
            pn = ds.PatientName
            sd = ds.StudyDate
            md = ds.Modality
            de = ds.StudyDescription
            self.dicom_file_info = "PatientName: " + str(pn) + "\n" + \
                                   "StudyDate: " + str(sd) + "\n" + \
                                   "Modality: " + str(md) + "\n" + \
                                   "StudyDescription: " + str(de)

            shape = ds.pixel_array.shape
            # Convert to float to avoid overflow or underflow losses.
            image_2d = ds.pixel_array.astype(float)
            # Rescaling grey scale between 0-255
            image_2d_scaled = (np.maximum(image_2d, 0) / image_2d.max()) * 255.0
            # Convert to uint
            image_2d_scaled = np.uint8(image_2d_scaled)
            # Write the PNG file
            with open(destination, 'wb') as png_file:
                w = png.Writer(shape[1], shape[0], greyscale=True)
                w.write(png_file, image_2d_scaled)
        except():
            pass
