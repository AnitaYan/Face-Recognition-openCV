#encoding=utf-8
import cv2
camera = cv2.VideoCapture(0)
facecas = cv2.CascadeClassifier("F:\openCVworkspace\haarcascade_frontalface_alt.xml")
faceid = 4  # 人脸标签
count = 1 # 每人采集100张

while True:
    ok, img = camera.read()
    if not ok:
        break
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    faces = facecas.detectMultiScale(gray, 1.3, 5)
    for (x, y, w, h) in faces:
        filename = "F:/openCVworkspace/dataset/User." + str(faceid) + "." + str(count) + ".jpg"
        count += 1
        cv2.imwrite(filename, gray[y:y+h, x:x+w])
        cv2.rectangle(img, (x, y), (x + w, y + h), (0, 255, 0), 5)
    cv2.imshow("win", img)
    if count > 100:
        break
    cv2.waitKey(33)
camera.release()
