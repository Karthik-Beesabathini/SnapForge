import cv2
import time

def capture_photos():
    cam = cv2.VideoCapture(0)
    photos = []

    for i in range(4):

        for j in range(3,0,-1):
            ret, frame = cam.read()
            temp = frame.copy()

            cv2.putText(temp,str(j),(250,250),
                        cv2.FONT_HERSHEY_SIMPLEX,7,(255,0,0),10)

            cv2.imshow("Countdown",temp)
            cv2.waitKey(1000)

        ret, frame = cam.read()
        photos.append(frame)
        time.sleep(1)

    cam.release()
    cv2.destroyAllWindows()

    return photos