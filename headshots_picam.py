import cv2
from picamera import PiCamera
from picamera.array import PiRGBArray

name = 'your_name' #replace with your name

cam = PiCamera()
cam.resolution = (512, 304)
cam.framerate = 10
rawCapture = PiRGBArray(cam, size=(512, 304))
    
img_counter = 0

while True:
    for frame in cam.capture_continuous(rawCapture, format="bgr", use_video_port=True):
        image = frame.array
        cv2.imshow("Press Space to take a photo", image)
        rawCapture.truncate(0)
    
        key = cv2.waitKey(1)
        rawCapture.truncate(0)
        if key == ord("q"): # q key pressed
            break
        elif key%256 == 32:
            # SPACE pressed
            img_name = "Datasets/"+ name +"/image_{}.jpg".format(img_counter)
            cv2.imwrite(img_name, image)
            print("{} written!".format(img_name))
            img_counter += 1
            
    if k%256 == 27:
        print("Escape hit, closing...")
        break

cv2.destroyAllWindows()
