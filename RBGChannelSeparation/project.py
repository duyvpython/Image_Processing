
import cv2
import numpy as np
lenaImage = cv2.imread("lena.png",cv2.IMREAD_COLOR)

imageHeight = len(lenaImage[0])
imageWidth = len(lenaImage[1])

redChannel=np.zeros((imageWidth
,imageHeight,3),np.uint8)
greenChannel=np.zeros((imageWidth,imageHeight,3),np.uint8)
blueChannel=np.zeros((imageWidth,imageHeight,3),np.uint8)

redChannel[:]=[0,0,0]
greenChannel[:]=[0,0,0]
blueChannel[:]=[0,0,0]

for x in range(imageWidth):
    for y in range(imageHeight):

        RED=lenaImage[x,y,2]
        GREEN=lenaImage[x,y,1]
        BLUE=lenaImage[x,y,0]
        
        redChannel[x,y,2]=RED
        greenChannel[x,y,1]=GREEN
        blueChannel[x,y,0]=BLUE

cv2.imshow("Lena image RBG origin",lenaImage)
cv2.imshow("Lena image channel RED",redChannel)
cv2.imshow("Lena image channel GREEN",greenChannel)
cv2.imshow("Lena image channel BLUE",blueChannel)

cv2.waitKey(0)

cv2.destroyAllWindows()
