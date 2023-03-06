import cv2
import numpy as np  
import PIL.Image as Image
import matplotlib.pyplot as plt



def imageGrayUsingLuminance(imagePIL):
    luminance = Image.new(imagePIL.mode,imagePIL.size)
    height = luminance.size[1]
    width = luminance.size[0]

    for x in range(width):
        for y in range(height):
            R, G, B = imagePIL.getpixel((x,y))
            gray = np.uint8(0.2121*R + 0.7152*G + 0.0722*B)
            luminance.putpixel((x,y),(gray, gray, gray))

    return luminance

def histogram(imageGrayPIL):
    his = np.zeros(256)
    height = imageGrayPIL.size[1]
    width = imageGrayPIL.size[0]

    for x in range(width):
        for y in range(height):
            gR, gG, gB = imageGrayPIL.getpixel((x,y))
            his[gR] += 1
    return his

def drawHistogramChart(his):
    width = 5
    height = 4
    plt.figure('Histogram chart image gray',figsize=(((width,height))),dpi=100)
    axisX = np.zeros(256)
    axisX = np.linspace(0,255,256) 
    plt.plot(axisX, his, color='orange')
    plt.title('Histogram chart')
    plt.xlabel('Value gray')
    plt.ylabel('Value point gray')
    plt.show()

imageLink = r'bird.jpg'

imagePIL = Image.open(imageLink)

imageGray = imageGrayUsingLuminance(imagePIL)

his = histogram(imageGray)

imageGrayLuminance = np.array(imageGray)

cv2.imshow("Image bird using average methor",imageGrayLuminance)
drawHistogramChart(his)

cv2.waitKey(0)
cv2.destroyAllWindows()
