# -*- coding: utf-8 -*-
"""
Created on Tue Jul 31 20:08:37 2018

@author: Fabian
"""


# -----------------------------------------------------------------------------
# IMPORTS
# -----------------------------------------------------------------------------
# from PIL import Image


"""BLANCO Y NEGRO DE UNA IMAGEN"""
def blanco_negro(im):
    # ruta = ("D:/Backup/FABI/Modelos/" + im)
    # im = Image.open(ruta)
    # im.show()
    bw = im
    i = 0
    while i < bw.size[0]:
        j = 0
        while j < bw.size[1]:
            r, g, b = bw.getpixel((i, j))
            gris = (r + g + b) / 3
            if gris < 100:
                bw.putpixel((i, j), (0, 0, 0))
            else:
                bw.putpixel((i, j), (255, 255, 255))
            j += 1
        i += 1
    return bw

"""ESCALA DE GRISES DE LA IMAGEN A COLOR"""
def escala_de_grises(im) :
    gris_im = im
    i = 0
    while i < gris_im.size[0]:
        j = 0
        while j < gris_im.size[1]:
            r, g, b = gris_im.getpixel((i,j))
            g = (r + g + b) / 3
            gris = int(g)
            pixel = tuple([gris, gris, gris])
            gris_im.putpixel((i,j), pixel)
            j+=1
        i+=1
    return gris_im


"""NEGATIVO DE LA IMAGEN A COLOR"""
def negativo_color(im):
    neg = im
    i = 0
    while i < neg.size[0]:
        j = 0
        while j < neg.size[1]:
            r, g, b = neg.getpixel((i,j))
            rn = 255 - r
            gn = 255 - g
            bn = 255 - b
            pixel = tuple([rn, gn, bn])
            neg.putpixel((i,j), pixel)
            j+=1
        i+=1
    return neg



