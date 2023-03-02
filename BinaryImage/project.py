import numpy as np
import cv2 
import PIL.Image as Image


imageLink = r'Lena.png'
imageLena = cv2.imread(imageLink,cv2.IMREAD_COLOR)

imagePIL = Image.open(imageLink)

imageLenaOrigin = Image.new(imagePIL.mode,imagePIL.size)
binaryImage = Image.new(imagePIL.mode,imagePIL.size)

width = imageLenaOrigin.size[0]
height = imageLenaOrigin.size[1]

limit = 130
for x in range(width):
    for y in range(height):
        R, G, B = imagePIL.getpixel((x,y))
        binary =np.uint8(0.2126*R + 0.7152*G + 0.0722*B)

        if(binary < limit):
            binaryImage.putpixel((x,y),(0,0,0))
        else:
            binaryImage.putpixel((x,y),(255, 255, 255))

binaryImageLena = np.array(binaryImage)

cv2.imshow('Image lena RBG Origin',imageLena)
cv2.imshow('Image lena using binary limit 130',binaryImageLena)

cv2.waitKey(0)
cv2.destroyAllWindows()
