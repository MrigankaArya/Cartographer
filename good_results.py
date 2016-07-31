from __future__ import division
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
        
    smallest = find_smallest(coordinates)
    #make a duplicate list to keep track of which coordinates
    #have already been calculated for a gradient check
    #if it's been part of a gradient check and the gradient coordinate list
    #is a good size, then the coordinates are removed from the list - they
    #don't belong in there anymore

    checklist = list(coordinates)
    #we dont want to check the gradient for something we're checking against
    checklist.remove(smallest)

    #hashmap functionality to hold the points sharing the same list of gradients
    #wrt the smallest point
    gradient_map = {}
    list_points = []

    gradient = 0
    for p in checklist:
        if p.x != smallest.x:
            gradient = round((p.y - smallest.y)/(p.x - smallest.x),2)
            
    

    
    
    
    plt.imshow(img),plt.show()


 #find the smallest x value for the 1st step of the algorithm
def find_smallest(coordinates):
    smallest = coordinates[0]
    place = 0
    for point in range (len(coordinates)):
        curr_x = coordinates[point].x
        if smallest.x > curr_x:
            place = point
            smallest = coordinates[point]
    return smallest
 

good_corners()
