import cv2
import numpy as np
print(cv2.__version__)

while True:
    frame = np.zeros([1000,1000,3],dtype=np.uint8)
    frame[:,:]= (255,0,255)
    cv2.imshow("my cv2",frame)
    if cv2.waitKey(1) == ord("q"):
        break
