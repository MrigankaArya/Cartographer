import numpy
import cv2
from PIL import Image
import numpy as np
from random import randint
from matplotlib import pyplot as plt

class Point:
    pass
    
def good_corners():
    img = cv2.imread('Z:/Cartographer/Test.png')
    gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
    blur = cv2.bilateralFilter(gray, 7, 175, 175)
    corners = cv2.goodFeaturesToTrack(blur,20,0.01,10)
    corners = np.int0(corners)

    #make a set to keep track of the coordinates that are detected
    coordinates = []
    
    for i in corners:
        x,y = i.ravel()
        point = Point()
        point.x = x
        point.y = y
        coordinates.append(point)
        cv2.circle(img,(x,y),3,255,-1)
        
    #find the smallest x value for the 1st step of the algorithm
    smallest = coordinates[0]
    place = 0
    for point in range (len(coordinates)):
        curr_x = coordinates[point].x
        if smallest.x > curr_x:
            place = point
            smallest = coordinates[point]
    
    same_gradient_list = []
    print smallest.x

    
    
    plt.imshow(img),plt.show()


    

good_corners()
