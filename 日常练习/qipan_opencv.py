import cv2
print(cv2.__version__)
import numpy as np
print(np.__version__)

qipan = int(input("棋盘的打算有多少： "))
size =  int(input("每个方块的大小打算是多少: "))
squres = int(qipan/size)

darkcolour = [0,0,0]
lightcolour = [0,0,255]
nowcolour = darkcolour

while True:
    x = np.zeros([qipan,qipan,3],dtype=np.uint8)
    for row in range(0,qipan):
        for cloums in range(0,qipan):
            x[size*row:size*(row+1),size*cloums:size*(cloums+1)]=nowcolour
            if nowcolour == lightcolour:
                nowcolour = darkcolour
            else:
                nowcolour = lightcolour
        if nowcolour == lightcolour:
            nowcolour = darkcolour
        else:
            nowcolour = lightcolour

    x = cv2.rectangle(x,(100,100),(800,800),(0,255,0),5)
    cv2.imshow("我的棋盘",x)

    if cv2.waitKey(1) == ord("q"):
        break
