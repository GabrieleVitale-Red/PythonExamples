import os
import cv2

from os import listdir
from skimage import io
from pyxelate import Pyx

#set the paths for the folders, source and destination
folder_dir = "./testimages"
folder_dir_destination = "./8bit/"

def init():
    # get the path for the source directory
    for images in os.listdir(folder_dir):
    
        # check if the image ends with jpg
        if (images.endswith(".jpg")):
            bitSampling(images)
        else:
            print("No images fuond")

def bitSampling(image):
    
    #load image with 'skimage.io.imread()'
    img = io.imread(folder_dir+"\\"+image)  
    downsample_by = 3  # new image will be 1/3th of the original in size
    palette = 9  # find 9 colors

    #1) Instantiate Pyx transformer
    pyx = Pyx(factor=downsample_by, palette=palette)

    #2) fit an image, allow Pyxelate to learn the color palette
    pyx.fit(img)

    #3) transform image to pixel art using the learned color palette
    new_image = pyx.transform(img)
    
    #save new image with 'skimage.io.imsave()'
    pathImage = folder_dir_destination+"\\"+image
    io.imsave(pathImage, new_image)

    # Read RGB image
    imgToShow = cv2.imread(pathImage)
    
    # Output img with window name as 'image'
    cv2.imshow("new", imgToShow)
    
    # Maintain output window utill
    # user presses a key
    cv2.waitKey(0)       
    
    # Destroying present windows on screen
    cv2.destroyAllWindows()

init()



    