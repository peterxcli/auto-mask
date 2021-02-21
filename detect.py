import RPi.GPIO as GPIO
import jetson.inference
import jetson.utils 
import cv2
import serial

net = jetson.inference.detectNet("ssd-mobilenet-v2", threshold=0.5)

ser = serial.Serial('/dev/ttyUSB0', 9600, timeout=10):

cap = cv2.VideoCapture(0)
state = 'open'
cnt = 0

while True:
	ret, img = cap.read()
	img_rgba = cv2.cvtColor(img, cv2.COLOR_BGR2RGBA)
	cuda_img = jetson.utils.cudaFromNumpy(img_rgba)
	detections = net.Detect(cuda_img, 1280, 720)
	person_appear = 0
	for detection in detections:
		print(net.GetClassDesc(detection.ClassID))
		if net.GetClassDesc(detection.ClassID) == 'person':
			person_appear = 1
	
	if person_appear == 1:
		state = 'close'
		ser.write(bytes('close\n','utf-8'))
	elif person_appear == 0 and state == 'close': 
		cnt += 1
		if cnt > 200:
			state = 'open'
			cnt = 0
			ser.write(bytes('open\n','utf-8'))

	key = cv2.waitKey(10)
	if key == 27:
		break
cv2.destroyAllWindows() 
cap.release()
GPIO.cleanup() 
