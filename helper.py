import os
import numpy as nup
import matplotlib.pyplot as pl
import cv2 as cv

# Get name list of all files in directory
def listImages():
    imagesAll = os.listdir()
    images = []
    for name in imagesAll:
        if (name.find('.jpg') > 0 or name.find('.jpeg') > 0 or name.find('.png') > 0):
            images.append(name)
    return images

# To Exclude a spasisfic channel from RGB
def rgbExclusion(image, channel):
    if channel == "r":
        image[:,:,2] = 0 
    elif channel == "g":
        image[:,:,1] = 0 
    elif channel == "b":
        image[:,:,0] = 0
    return image

# Implmantion of Convolution from scratch
def myConvolve2d(image, kernel):
    output = nup.zeros_like(image)            # output
    
    image_padded = nup.zeros((image.shape[0] + 2, image.shape[1] + 2)) # create frame all zeros and padded space   
    image_padded[1:-1, 1:-1] = image # copy image between padded space
    
    for x in range(image.shape[0]):     # Loop over every pixel of the image
        for y in range(image.shape[1]):
            # element-wise multiplication and summation 
            output[x,y]=(kernel*image_padded[x:x+3,y:y+3]).sum()
    return output

# Display two RGB images side by side
def displayTwoImage(image1, title1, image2, title2):
    pl.rcParams['figure.figsize'] = (20.0, 16.0) # set default size of plots
    fig = pl.figure()
    fig.add_subplot(1, 2, 1)
    pl.imshow(cv.cvtColor(image1,cv.COLOR_BGR2RGB))
    pl.title(title1)
    fig.add_subplot(1, 2, 2)
    pl.imshow(cv.cvtColor(image2,cv.COLOR_BGR2RGB))
    pl.title(title2)

# Display Two Gray Scale Images
def displayTwoConvImages(image1, title1, image2, title2):
    pl.rcParams['figure.figsize'] = (20.0, 16.0) # set default size of plots
    fig = pl.figure()
    fig.add_subplot(1, 2, 1)
    pl.imshow(image1,cmap=pl.cm.gray)
    pl.title(title1)

    fig.add_subplot(1, 2, 2)
    pl.imshow(image2,cmap=pl.cm.gray)
    pl.title(title2)
    
# Dispaly four RGB images side by side 
def displayFourImage(image1, title1, image2, title2, image3, title3, image4, title4):
    pl.rcParams['figure.figsize'] = (20.0, 16.0) # set default size of plots
    fig = pl.figure()
    fig.add_subplot(1, 4, 1)
    pl.imshow(cv.cvtColor(image1,cv.COLOR_BGR2RGB))
    pl.title(title1)
    fig.add_subplot(1, 4, 2)
    pl.imshow(cv.cvtColor(image2,cv.COLOR_BGR2RGB))
    pl.title(title2)
    fig.add_subplot(1, 4, 3)
    pl.imshow(cv.cvtColor(image3,cv.COLOR_BGR2RGB))
    pl.title(title3)
    fig.add_subplot(1, 4, 4)
    pl.imshow(cv.cvtColor(image4,cv.COLOR_BGR2RGB))
    pl.title(title4)