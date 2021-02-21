cap = cv2.VideoCapture(gst_pipeline, cv2.CAP_GSTREAMER)
import cv2
gst_pipeline = ("nvarguscamerasrc ! "
                "video/x-raw(memory:NVMM), "
                "width=3820, height=2464, "
                "format=(string)NV12, framerate=21/1 ! "
                "nvvidconv flip-method=0 ! "
                "video/x-raw, width=1920, height=1080, format=(string)BGRx ! "
                "videoconvert ! "
                "video/x-raw, format=(string)BGR ! appsink"
                )

cap = cv2.VideoCapture(gst_pipeline, cv2.CAP_GSTREAMER)
while True:
    ret, img = cap.read()
    cv2.imshow("input", img)

    key = cv2.waitKey(10)
    if key == 27:
        break


cv2.destroyAllWindows() 
cap.release()
