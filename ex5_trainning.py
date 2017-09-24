#encoding=utf-8
import cv2
import os
import numpy
path = "dataset"
filenames = os.listdir(path) #得到目录下所有文件
faceSample = [] #样本集合
ids= [] #标签集合
lbpclassifier = cv2.face.createLBPHFaceRecognizer()
for file in filenames:
    #print (file)
    img = cv2.imread(path+"/"+file,0)
    img = cv2.resize(img,(32,32))
    id = int(os.path.split(file)[-1].split('.')[1])
    #print (id)
    faceSample.append(img) #加入集合
    ids.append(id)
#print(faceSample)
#print(ids)
lbpclassifier.train(numpy.array(faceSample),numpy.array(ids))
lbpclassifier.save("facetrainer.xml")