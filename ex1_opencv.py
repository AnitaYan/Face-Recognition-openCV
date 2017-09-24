#encoding = utf-8

import cv2  #导入opencv库

img = cv2.imread("cat1.jpg")    #pyton变量不需要定义类型
#img = cv2.imread("cat1.jpg",1)
cv2.imshow("win",img)   #显示图片，窗口名，变量
cv2.waitKey(0)  #等待用户输入按键
print(img.size)     #756900
print(img.shape)    #(435, 580, 3)
# 通道数：彩色图像（RGB 都是0~255）、黑白图像（0,255）、灰度图像（0~255）

