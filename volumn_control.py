import cv2 
import time 
import HandTrackingModule as htm

# changing volumn accordingly - only works on linux ! 
from subprocess import call 
def set_volumn(percentage) : 
    call(["amixer", "-D", "pulse", "sset", "Master", str(percentage)+"%"])


cap = cv2.VideoCapture(0) 
prev_time = 0 
detector = htm.handDetector()	

while True : 

	sec , img = cap.read() 
	img = detector.findHands(img , True) 
	lm = detector.findPosition(img) 

	if len(lm) != 0 : 
		length = detector.findDistance(4 , 8 , img , True)[0] 
		set_volumn(length / 300 * 100)

	curr_time = time.time()
	fps = 1 / (curr_time - prev_time) 
	prev_time = curr_time 	
	
	cv2.putText(img , "FPS : " + str(int(fps)) , (50, 50) , cv2.FONT_HERSHEY_COMPLEX , 1 , (0 , 0 , 255) , 2)		
	cv2.imshow('cam' , img) 
	cv2.waitKey(1)
 
	

