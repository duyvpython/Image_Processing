import numpy as np
import cv2
import PIL.Image as Image

imageLink = r'lena.png'
imageLena = cv2.imread(imageLink,cv2.IMREAD_COLOR)
imagePIL = Image.open(imageLink)

imageLenaOrigin=Image.new(imagePIL.mode,imagePIL.size)
average = Image.new(imagePIL.mode,imagePIL.size)
lightness = Image.new(imagePIL.mode,imagePIL.size)
luminance = Image.new(imagePIL.mode,imagePIL.size)
width = imageLenaOrigin.size[0]
height = imageLenaOrigin.size[1]

#Average method
for x in range(width):
    for y in range(height):
        R,G,B = imagePIL.getpixel((x,y))
        gray = np.uint8((R+G+B)/3)
        average.putpixel((x,y),(gray,gray,gray))

imageGrayAverage =np.array(average)

#Lightness method
for x in range(width):
    for y in range(height):
        R,G,B = imagePIL.getpixel((x,y))
        MIN = min(R,G,B)
        MAX = max(R,G,B)
        gray = np.uint8((MIN+MAX)/2)
        lightness.putpixel((x,y),(gray,gray,gray))

imageGrayLightness =np.array(lightness)

#Luminance method
for x in range(width):
    for y in range(height):
        R,G,B = imagePIL.getpixel((x,y))
        gray = np.uint8(0.2121*R + 0.7152*G + 0.0722*B)
        luminance.putpixel((x,y),(gray,gray,gray))

imageGrayLuminance =np.array(luminance)

cv2.imshow('image lena origin RGB ',imageLena)
cv2.imshow('image gray using Average',imageGrayAverage)
cv2.imshow('image gray using Lightness',imageGrayLightness)
cv2.imshow('imgae gray using Luminace',imageGrayLuminance)

cv2.waitKey(0)
cv2.destroyAllWindows()