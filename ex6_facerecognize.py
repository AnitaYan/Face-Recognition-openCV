#encoding=utf-8
import cv2
camera = cv2.VideoCapture(0)
facecas = cv2.CascadeClassifier("F:\openCVworkspace\haarcascade_frontalface_alt.xml")
recognizer = cv2.face.createLBPHFaceRecognizer()
recognizer.load("facetrainer.xml")

while True:
    ok, img = camera.read()
    if not ok:
        break
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    faces = facecas.detectMultiScale(gray, 1.3, 5)
    for (x,y,w,h) in faces:
        cv2.rectangle(img, (x, y), (x + w, y + h), (0, 255, 0), 5)
        roi = gray[y:y+h, x:x+w]
        roi = cv2.resize(roi, (32, 32))
        id = recognizer.predict(roi)
        name = None
        if id[0] == 1:
            name = "yingxue"
        elif id[0] == 2:
            name = "shasha"
        elif id[0] == 3:
            name = "yiwen"
        elif id[0] == 4:
            name = "jiaxuan"
        print(id)
        font = cv2.FONT_HERSHEY_SIMPLEX
        color = (0, 255, 0);
        cv2.putText(img, name, (x, y), font, 2, color, 5)
    cv2.imshow("win", img)
    cv2.waitKey(33)
camera.release()
