#encoding = utf-8

import cv2  #导入opencv库

#视频处理类 0 1 2 3.。
camera = cv2.VideoCapture(0)    #0表示默认摄像头
while True:
    ok,image = camera.read()
    if not ok:  #采集失败，跳出循环
        break
    cv2.imshow("win",image)
    cv2.waitKey(33) #等待33毫秒