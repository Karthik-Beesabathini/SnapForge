import numpy as np
import cv2
import os


def create_collage(photos):

    collage=np.hstack(((photos[0],photos[1],photos[2])))
    collage1=np.hstack((photos[3],photos[4],photos[5]))
    collage2=np.vstack((collage,collage1))

    if not os.path.exists("collage"):
        os.makedirs("collage")

    path="collage/collages.jpg"

    cv2.imwrite(path,collage2)

    return path
def create_collage1(photos1):

    collage=np.hstack((photos1[0],photos1[1]))
    collage1=np.hstack((photos1[2],photos1[3]))
    collage2=np.vstack((collage,collage1))

    if not os.path.exists("collage"):
        os.makedirs("collage")

    path="collage/collages.jpg"

    cv2.imwrite(path,collage2)

    return path
def create_collage2(photos2):

    collage=np.hstack((photos2[0],photos2[1],photos2[2]))

    if not os.path.exists("collage"):
        os.makedirs("collage")

    path="collage/collages.jpg"

    cv2.imwrite(path,collage)

    return path
def create_collage3(photos3):

    collage=np.hstack((photos3[0],photos3[1]))

    if not os.path.exists("collage"):
        os.makedirs("collage")

    path="collage/collages.jpg"

    cv2.imwrite(path,collage)

    return path