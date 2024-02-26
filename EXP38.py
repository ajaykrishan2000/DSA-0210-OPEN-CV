import cv2
img = cv2.imread(r"C:\Users\subak\OneDrive\Pictures\Saved Pictures\WIN_20220307_10_15_40_Pro.jpg")
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
face_cascade =cv2.CascadeClassifier(r"C:\Users\subak\OneDrive\Documents\Open CV\Img & Vid Material\haarcascade_frontalface_default.xml")
faces = face_cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=5)
for (x, y, w, h) in faces:
    cv2.rectangle(img, (x, y), (x + w, y + h), (0, 255, 0), 2)
    img1 = cv2.resize(img,(600,600))
    cv2.imshow('Faces Detected', img1)
cv2.waitKey(0)
cv2.destroyAllWindows()
