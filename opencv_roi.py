import cv2
print(cv2.__version__)
width=640
height=520
cam=cv2.VideoCapture(0,cv2.CAP_DSHOW)
cam.set(cv2.CAP_PROP_FRAME_WIDTH, width)
cam.set(cv2.CAP_PROP_FRAME_HEIGHT,height)
cam.set(cv2.CAP_PROP_FPS, 30)
cam.set(cv2.CAP_PROP_FOURCC,cv2.VideoWriter_fourcc(*'MJPG'))
while True:
    ignore,  frame = cam.read()
    cv2.imshow('my WEBcam', frame)
    cv2.moveWindow('my WEBcam',0,0)

    frameGray = cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
    cv2.imshow("my Gray",frameGray)
    cv2.moveWindow("my Gray",650,0)

    frameBGR = frame[150:210,250:390]
    cv2.imshow('my frameBGR', frameBGR)
    row = 0
    colume = 0
    cv2.moveWindow('my frameBGR',row,colume)

    if cv2.waitKey(1) & 0xff ==ord('q'):
        break
cam.release()