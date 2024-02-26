import cv2
import numpy as np
p=r"C:\Users\subak\OneDrive\Documents\Open CV\Img & Vid Material\Sample2.mp4"
c= cv2.VideoCapture(p)
p1=np.float32([[56,65],[368,52],[28,387],[389,390]])
p2= np.float32([[100,50],[300,0],[0,300],[300,300]])
m= cv2.getPerspectiveTransform(p1,p2)

    

while True:
    a,r= c.read()
    r1=cv2.resize(r,(700,700))
    d= cv2.warpPerspective(r1,m,(700,700))
    cv2.imshow("a",d)
    cv2.waitKey(1)
