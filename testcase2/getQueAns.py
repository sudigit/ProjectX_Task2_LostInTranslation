import numpy as np
import cv2

img = cv2.imread('combine1.jpg',cv2.IMREAD_COLOR)

gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)

cv2.imwrite('gray.jpg', gray)

ret,thresh = cv2.threshold(gray,0,255,cv2.THRESH_BINARY)
cv2.imwrite('blackwhite.jpg',thresh)

kernel = np.ones((5, 5), np.uint8)
eroded = cv2.erode(thresh, kernel, iterations=12)
cv2.imwrite('eroded.jpg', eroded)

height=2000
width=1414
h=int(height/14)
w=int(width/6)
#print (h)
#print(w)

coords=[]
y=0
while y<2000:
    for x in range(width):
        if eroded[y,x]>0:
            coords.append((x,y))
            if y+h>=height or x+w>=width:
                if y+h>=height:
                    x+=w
                if x+w>=width:
                    y+=h
            else:
                x+=w
                y+=h
        x+=1
    y+=1

#print(coords)


def queans(coord):
    x,y=coord
    match x:
        case x if x in range(1*w, 2*w):
            a="A"
        case x if x in range(2*w, 3*w):
            a="B"
        case x if x in range(4*w, 5*w):
            a="C"
        case x if x in range(5*w, 6*w):
            a="D"
        case _:
            a=None
        
    match y:
        case y if y in range(2*h, 3*h):
            q=1
        case y if y in range(3*h, 4*h):
            q=2
        case y if y in range(4*h, 5*h):
            q=3
        case y if y in range(5*h, 6*h):
            q=4
        case y if y in range(6*h, 7*h):
            q=5
        case y if y in range(7*h, 8*h):
            q=6
        case y if y in range(8*h, 9*h):
            q=7
        case y if y in range(9*h, 10*h):
            q=8
        case y if y in range(10*h, 11*h):
            q=9
        case y if y in range(11*h, 12*h):
            q=10
        case _:
            q=None    

    return (q,a)



qa=[]
for k in coords:
    qa.append(queans(k))

print(qa)

cv2.waitKey(0)
cv2.destroyAllWindows()

