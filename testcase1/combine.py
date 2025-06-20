import cv2
import numpy as np

images1=[cv2.imread("Bhaskar.jpg"), cv2.imread("Raghav.jpg"), cv2.imread("Ganshyam.jpg")] 
images2=[cv2.imread("Chintan.jpg"), cv2.imread("Omkar.jpg"), cv2.imread("Yash.jpg")]

height, width = images1[0].shape[:2]
print(height, width)
#height, width = images1[1].shape[:2]
#print(height, width)
#height, width = images1[2].shape[:2]
#print(height, width)
#height, width = images2[0].shape[:2]
#print(height, width)
#height, width = images2[1].shape[:2]
#print(height, width)
#height, width = images2[2].shape[:2]
#print(height, width)

image1 = np.zeros((height, width,3), dtype=np.uint8)
for y in range(0,height):
    for x in range(0,width):
        for i in range(0,3):
                image1[y,x][i] = images1[0][y,x][i] + images1[1][y,x][i] + images1[2][y,x][i]

cv2.imwrite("combine1.jpg", image1)

image2 = np.zeros((height, width, 3), dtype=np.uint8)
for y in range(0,height):
    for x in range(0,width):
        for i in range(0,3):
                image2[y,x] = images2[0][y,x] + images2[1][y,x] + images2[2][y,x]
cv2.imwrite("combine2.jpg", image2)


cv2.waitKey(0)
cv2.destroyAllWindows()