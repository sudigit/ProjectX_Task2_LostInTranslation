import numpy as np
import cv2

#get combined image
img=cv2.imread('combine1.jpg')

#convert to grayscale
gray=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
cv2.imwrite('gray.jpg', gray)

#convert to black and white
ret,thresh = cv2.threshold(gray,0,255,cv2.THRESH_BINARY)
cv2.imwrite('blackwhite.jpg',thresh)

#erosion
kernel = np.ones((5, 5), np.uint8)
eroded = cv2.erode(thresh, kernel, iterations=12)
cv2.imwrite('eroded.jpg', eroded)

height, width = eroded.shape[:2] 
h=int(height/10)
w=int(width/7)
#print (h)
#print(w)

#get coords when white pixels encountered then skip rows and columns
coords=[]
y=0
que=0
while y<height:
    for x in range(width):
        if eroded[y,x]>0:
            que+=1
            coords.append((x,y,que))
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


# assign que and ans
def queans(coord):
    x,y,q=coord

    match x:
        case x if x in range(1*w, 2*w):
            a="A"
        case x if x in range(3*w, 4*w):
            a="B"
        case x if x in range(5*w, 6*w):
            a="C"
        case x if x in range(6*w, 7*w):
            a="D"
        case _:
            a=None
        

    return (q,a)

#print que and ans
qa=[]
for k in coords:
    qa.append(queans(k))

print (qa)

cv2.waitKey(0)
cv2.destroyAllWindows()