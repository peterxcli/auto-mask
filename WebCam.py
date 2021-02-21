import cv2

cap = cv2.VideoCapture(0)
while True:
    ret, img = cap.read()
    cv2.imshow("input", img)

    key = cv2.waitKey(10)
    if key == 27:
        break


cv2.destroyAllWindows() 
cap.release()
