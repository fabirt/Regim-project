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
import cv2


def resource_path(relative_path):
    if hasattr(sys, '_MEIPASS'):
        return os.path.join(sys._MEIPASS, relative_path)
    return os.path.join(os.path.abspath("."), relative_path)


def match(file_reference, file_input):
    MAX_FEATURES = 500
    GOOD_MATCH_PERCENT = 0.15

    imReference = cv2.imread(file_reference, cv2.IMREAD_COLOR)
    imInput = cv2.imread(file_input, cv2.IMREAD_COLOR)

    # Convert images to gray scale
    im1Gray = cv2.cvtColor(imReference, cv2.COLOR_BGR2GRAY)
    im2Gray = cv2.cvtColor(imInput, cv2.COLOR_BGR2GRAY)

    # Detect ORB features and compute descriptors.
    orb = cv2.ORB_create(MAX_FEATURES)
    keypoints1, descriptors1 = orb.detectAndCompute(im1Gray, None)
    keypoints2, descriptors2 = orb.detectAndCompute(im2Gray, None)

    # Match features.
    matcher = cv2.DescriptorMatcher_create(cv2.DESCRIPTOR_MATCHER_BRUTEFORCE_HAMMING)
    # matcher = cv2.BFMatcher(cv2.NORM_HAMMING, crossCheck=True)
    matches = matcher.match(descriptors1, descriptors2, None)

    # Sort matches by score
    matches.sort(key=lambda x: x.distance, reverse=False)

    # Remove not so good matches
    numGoodMatches = int(len(matches) * GOOD_MATCH_PERCENT)
    matches = matches[:numGoodMatches]

    # Draw top matches
    imMatches = cv2.drawMatches(imReference, keypoints1, imInput, keypoints2, matches, None, flags=2)

    return imMatches
