
import numpy
import cv2
from PIL import Image
import numpy as np
from matplotlib import pyplot as plt

def detect_verts():
    fname = 'Z:/Cartographer/Kyoto.jpg'
    img = cv2.imread(fname)
    blur = cv2.bilateralFilter(img, 9, 75, 75)

    gray = cv2.cvtColor(blur, cv2.COLOR_BGR2GRAY)

    gray = np.float32(gray)
    dst = cv2.cornerHarris(gray,2,3,0.04)

    dst = cv2.dilate(dst, None)

    blur[dst>0.01*dst.max()] = [0,0,255]

    cv2.imshow('dst', blur)
    if cv2.waitKey(0) & 0xff == 27:
        cv2.destroyAllWindows()

#detect_verts()

def good_corners():
    img = cv2.imread('Z:/Cartographer/kyoto.jpg')
    gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
    blur = cv2.bilateralFilter(gray, 7, 175, 175)
    corners = cv2.goodFeaturesToTrack(blur,20,0.01,10)
    corners = np.int0(corners)

    for i in corners:
        x,y = i.ravel()
        cv2.circle(img,(x,y),3,255,-1)
        print x,y

    plt.imshow(img),plt.show()

#good_corners()

def cartoon_detection():
    num_down = 2
    num_bilateral = 7

    img_rgb = cv2.imread('Z:/Cartographer/kyoto.jpg')

    # downsampling using Gaussian pyramid
    img_color = img_rgb
    for _ in xrange(num_down):
        img_color = cv2.pyrDown(img_color)

    # small bilateral filter repeatedly applied
    for _ in xrange(num_bilateral):
        img_color = cv2.bilateralFilter(img_color, 29, 20, 7)

    # upsample to original size
    for _ in xrange(num_down):
        img_color = cv2.pyrUp(img_color)

    # convert to gray
    gray = cv2.cvtColor(img_rgb, cv2.COLOR_RGB2GRAY)
    gray = np.float32(gray)

    # detect corners
    dst = cv2.cornerHarris(gray,2,3,0.04)

    dst = cv2.dilate(dst, None)
    print(dst)

    img_rgb[dst>0.01*dst.max()] = [0,0,255]
    
    # show
    cv2.imshow('dst', img_rgb)
    if cv2.waitKey(0) & 0xff == 27:
        cv2.destroyAllWindows()


cartoon_detection()
    
