import cv2
print(cv2.__version__)
evt = 0
def mouseClick(event,xPOS,yPOS,flags,params):
    # event,xPOS,yPOS
    global pnt1
    global pnt2
    global evt
    if event == cv2.EVENT_LBUTTONDOWN:
        print(event)
        pnt1 = (xPOS,yPOS)
        # print(pnt1)
        evt = event
    if event == cv2.EVENT_LBUTTONUP:
        print(event)
        pnt2 = (xPOS,yPOS)
        evt = event
    if event == cv2.EVENT_RBUTTONUP:
        evt == event
width=640
height=520
cam=cv2.VideoCapture(0,cv2.CAP_DSHOW)
cam.set(cv2.CAP_PROP_FRAME_WIDTH, width)
cam.set(cv2.CAP_PROP_FRAME_HEIGHT,height)
cam.set(cv2.CAP_PROP_FPS, 30)
cam.set(cv2.CAP_PROP_FOURCC,cv2.VideoWriter_fourcc(*'MJPG'))
cv2.namedWindow("my WEBcam")
cv2.setMouseCallback("my WEBcam",mouseClick)
while True:
    ignore,  frame = cam.read()
    if evt == 4 and pnt1 != pnt2:
        cv2.rectangle(frame,pnt1,pnt2,(0,0,255),2)
        # 绘制一个ROI兴趣
        ROI = frame[pnt1[0]:pnt2[0],pnt1[1]:pnt2[1]]
        cv2.imshow("my ROI",ROI)
        cv2.moveWindow("my ROI",int(width*1.1),0)
    if evt == 5:
        cv2.destroyWindow('my ROI')

    cv2.imshow('my WEBcam', frame)
    cv2.moveWindow('my WEBcam',0,0)
    # frameGray = cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
    # cv2.imshow("my Gray",frameGray)
    # cv2.moveWindow("my Gray",650,0)
    # frameBGR = frame[250:520,25:520]
    # cv2.imshow('my frameBGR', frameBGR)
    # row = 0
    # colume = 0
    # cv2.moveWindow('my frameBGR',row,colume)
    if cv2.waitKey(1) & 0xff ==ord('q'):
        break
cam.release()