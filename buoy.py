import cv2
import matplotlib
import numpy as np
import argparse
import imutils
import cv

# to support command line input of image
ap = argparse.ArgumentParser()
ap.add_argument("-i", "--image", required=True,
	help="path to the input image")
args = vars(ap.parse_args())

#functions to gray, blur, equalize and hsv_split of image
def gray(image):
	gray_img = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
	return gray_img

def blur(image):
	blurred_img = cv2.GaussianBlur(image, (11, 11), 0)
	return blurred_img

def equalize(image):
	equalized_img = cv2.equalizeHist(image)
	return equalized_img

def hsv_split(image):
	hsv_img = cv2.cvtColor(img, cv2.COLOR_RGB2HSV)
	h, s, v = cv2.split(hsv_img)
	return hsv_img, h, s, v

def binary_thresh(image):
	ret, thresh = cv2.threshold(image, 60, 255, cv2.THRESH_BINARY)
	return thresh

def erodeAndDilate(img):
	img = binary_thresh(blur(gray(img)))
	img = cv2.erode(img, np.ones((8,8)))
	img = cv2.dilate(img, np.ones((8,8)))
	return img

def get_circles(color):
	re = maskres_dict[color][0]
	re = binary_thresh(re)
	re = cv2.Canny(re, 100, 200)
	re = binary_thresh(re)
	circles = cv2.HoughCircles(re,cv2.cv.CV_HOUGH_GRADIENT,1,75,param1=50,param2=13,minRadius=0,maxRadius=175)
	return circles

def extractMaxRadius(arr):
	#array of n*3 dim
	pos = max(enumerate(arr[:,2]), key = lambda x: x[1])[0]
	return arr[0]

#setting HSV ranges for color thresholding
ranges={
	'lower_red' : np.array([100,100,100]),
	'upper_red' : np.array([130,255,255]),
	'lower_yellow' : np.array([65,125,125]),
	'upper_yellow' : np.array([100,255,255]),
	'lower_green' : np.array([40,10,10]),
	'upper_green' : np.array([70,255,255]),
	'lower_blue' : np.array([0,100,100]),
	'upper_blue' : np.array([30,255,255])}

#function to return mask and res given a color
def color_mask(img,hsv_image, color):
	
	if color == "R" or color=="r":
		lower, upper = ranges['lower_red'], ranges['upper_red']
	elif color == "B" or color=="b":
		lower, upper = ranges['lower_blue'], ranges['upper_blue']
	elif color == "G" or color=="g":
		lower, upper = ranges['lower_green'], ranges['upper_green']
	elif color == "Y" or color=="y":
		lower, upper = ranges['lower_yellow'], ranges['upper_yellow']
	else:
		return 0,0
	mask = cv2.inRange(hsv_image, lower, upper)
	res = cv2.bitwise_and(img, img, mask=mask)
	#print(lower, upper)
	return mask, res

#-----execution with buoysf.jpg-----#
img = cv2.imread(args["image"])
hsv_img, h, s, v = hsv_split(blur(img))
maskres_dict={}
for c in "gyr":
	mask, res = color_mask(img, hsv_img, c)
	maskres_dict[c] = [mask, res]


green_circles = get_circles('g')
green_circles = np.round(green_circles[0,:]).astype("int")
green_circles = extractMaxRadius(green_circles)

red_circles = get_circles('r')
red_circles = np.round(red_circles[0,:]).astype("int")
red_circles = extractMaxRadius(red_circles)

yellow_circles = get_circles('y')
yellow_circles = np.round(yellow_circles[0,:]).astype("int")
yellow_circles = extractMaxRadius(yellow_circles)

circles_dict={}
circles_dict['red'] = red_circles
circles_dict['yellow'] = yellow_circles
circles_dict['green'] = green_circles

for each in circles_dict:
	i = circles_dict[each]
	cv2.circle(img,(i[0],i[1]),i[2],(0,255,0),2)
	cv2.rectangle(img, (i[0] - 1, i[1] - 1), (i[0] + 2, i[1] + 2), (0, 128, 255), -1)
	cv2.putText(img, each +' x: '+str(i[0])\
					  +' y: '+str(i[1])\
					  +' r: '+str(i[2]), (i[0]-50,i[1]+40), cv2.FONT_HERSHEY_SIMPLEX, 0.4, \
					  (0,0,0),2)
cv2.imshow("targets", img)
cv2.imwrite("target-buoys.jpg",img)
cv2.waitKey(0)