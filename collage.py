import numpy as np
import cv2
import os

def create_collage(photos):

    collage=np.hstack((photos[0],photos[1]))
    collage1=np.hstack((photos[2],photos[3]))
    collage2=np.vstack((collage,collage1))

    if not os.path.exists("collage"):
        os.makedirs("collage")

    path="collage/collages.jpg"

    cv2.imwrite(path,collage2)

    return path