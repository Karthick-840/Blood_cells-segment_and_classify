import cv2
import numpy as np

img = cv2.imread('Sa_094.jpg')

# Measuring the image dimensions
height, width = img.shape[:2]
imgarea = np.multiply(height, width)

# Converting image to grayscale and finding the edges of the objects
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
edged = cv2.Canny(gray, 200, 200, apertureSize=3)

# Finding the contours in the image to extract the grid
cnts = cv2.findContours(edged, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
cnts = cnts[0] if len(cnts) == 2 else cnts[1]

# Initializing and storing the area of
# the squares of the grid (which we can find by finding only the area's that are not too small or too large)
# in an array
sqarea = np.array([])

for c in cnts:
    cv2.drawContours(img, [c], 0, (0, 255, 0), 3)
    area = cv2.contourArea(c)

    if imgarea/10000 < area < imgarea/500:
        sqarea = np.append(sqarea, area)

cv2.imwrite('grid.jpg', img)

# Measuring the mean area of the grid
gridarea = np.mean(sqarea)
print(gridarea)

# Calculating the amount of pixels per cm in the image
pixelspercm = np.sqrt(gridarea)
print(pixelspercm)
