import cv2
print(cv2.__version__)

cam = cv2.VideoCapture(0)
cam2 = cv2.VideoCapture(1)

while True:
    ignore,frame = cam.read()
    # frame1 = cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
    cv2.imshow("my cam",frame)
    cv2.moveWindow("my cam",0,0)

    ignore,Lframe = cam2.read()
    # Lframe1 = cv2.cvtColor(Lframe,cv2.COLOR_BayerRG2GRAY)
    cv2.imshow("my cam2",Lframe)
    cv2.moveWindow("my cam2",720,0)

    if  cv2.waitKey(1) == ord("q"):
        break
    
cam.release()