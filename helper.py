import os
import numpy as nup
# Get name list of all files in directory
def listImages():
    imagesAll = os.listdir()
    images = []
    for name in imagesAll:
        if (name.find('.jpg') > 0 or name.find('.jpeg') > 0 or name.find('.png') > 0):
            images.append(name)
    return images

def rgbExclusion(image, channel):
    if channel == "r":
        image[:,:,2] = 0 
    elif channel == "g":
        image[:,:,1] = 0 
    elif channel == "b":
        image[:,:,0] = 0
    return image

def myConvolve2d(image, kernel):
    output = nup.zeros_like(image)            # output
    
    image_padded = nup.zeros((image.shape[0] + 2, image.shape[1] + 2)) # create frame all zeros and padded space   
    image_padded[1:-1, 1:-1] = image # copy image between padded space
    
    for x in range(image.shape[0]):     # Loop over every pixel of the image
        for y in range(image.shape[1]):
            # element-wise multiplication and summation 
            output[x,y]=(kernel*image_padded[x:x+3,y:y+3]).sum()
    return output