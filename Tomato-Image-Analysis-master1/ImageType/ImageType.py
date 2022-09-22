import cv2

img = cv2.imread('Images/SR_003.jpg')

# Converting image to grayscale and finding the edges of the objects
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
edged = cv2.Canny(gray, 200, 200, apertureSize=3)

# Finding the contours in the image to extract the grid
cnts = cv2.findContours(edged, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
cnts = cnts[0] if len(cnts) == 2 else cnts[1]

for c in cnts:
    cv2.drawContours(img, [c], 0, (0, 255, 0), 3)

if (len(cnts)) > 3000:
    ImageType = "Grid"
else:
    ImageType = "Non grid"

print(ImageType)
print(len(cnts))
# cv2.imwrite('contour2.jpg', img)


