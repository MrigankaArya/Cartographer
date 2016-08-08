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
    dict_gradient_maps = {}
    
    for i in corners:
        x,y = i.ravel()
        point = Point()
        point.x = x
        point.y = y
        coordinates.append(point)
        cv2.circle(img,(x,y),3,255,-1)

    while len(coordinates ) > 2 :
        smallest = find_smallest(coordinates)
        #if it's been part of a gradient check and the gradient coordinate list
        #is a good size, then the coordinates are removed from the list - they
        #don't belong in there anymore
        #we dont want to check the gradient for something we're checking against
        coordinates.remove(smallest)
        dict_gradient_maps[smallest] = gradients(coordinates)
        
    dict_gradient_maps = {key: value for key, value in dict_gradient_maps.items() if len(value) > 0}    
    plt.imshow(img),plt.show()
    print dict_gradient_maps


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


def gradients(checklist):
    gradient_map = {}
    smallest = find_smallest(checklist)
    gradient = 0
    for p in checklist:
        if p.x == smallest.x:
            continue

        gradient = round((p.y - smallest.y)/(p.x - smallest.x),1)

        if gradient in gradient_map:
            gradient_map[gradient].append(p)
        else:
            gradient_map[gradient] = [p]

    print gradient_map
    #Removing gradients with only 1 point in the thingy
    condensed_map = {key: value for key, value in gradient_map.items() if len(value) > 1}
    print "----------------------------------------------"
    return condensed_map

good_corners()
