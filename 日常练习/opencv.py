import cv2
print(cv2.__version__)

rows = int(input("请告诉我你需要的行数： "))
columes = int(input("请告诉我你需要的列数: "))
cam = cv2.VideoCapture(0,cv2.CAP_DSHOW)
width = 512
height = 512
cam.set(cv2.CAP_PROP_FRAME_WIDTH,width) 
cam.set(cv2.CAP_PROP_FRAME_HEIGHT,height)
cam.set(cv2.CAP_PROP_FPS,30)
cam.set(cv2.CAP_PROP_FOURCC,cv2.VideoWriter_fourcc(*'MJPG'))
# 罗技相机
# cam2 = cv2.VideoCapture(1)
while True:
    ignore,frame = cam.read()
    frame=cv2.resize(frame,(int(width/columes),int(height/columes)))
    # 设置相机的显示效果
    # frame1 = cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
    for i in range(0,rows):
        for j in range(0,columes):
            windowname = "windows"+ str(i) +  str(j)
            cv2.imshow(windowname,frame)
            cv2.moveWindow(windowname,int((width/columes) * j),int((height/columes+60) * i ))    
        # cv2.imshow("my cam",frame)
    # cv2.moveWindow("my cam",0,0)
    # ignore,Lframe = cam2.read()
    # Lframe1 = cv2.cvtColor(Lframe,cv2.COLOR_BayerRG2GRAY)
    # cv2.imshow("my cam2",Lframe)
    # cv2.moveWindow("my cam2",720,0)
    if  cv2.waitKey(1) == ord("q"):
        break  
cam.release()