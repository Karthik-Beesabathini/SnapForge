import cv2
import time

def capture_photos():
    cam = cv2.VideoCapture(0)
    photos = []

    for i in range(6):

        for j in range(3,0,-1):
            ret, frame = cam.read()
            temp = frame.copy()

            cv2.putText(temp,str(j),(250,250),
                        cv2.FONT_HERSHEY_SIMPLEX,7,(250,0,0),10)

            cv2.imshow("Countdown",temp)
            cv2.waitKey(1000)

        ret, frame = cam.read()
        photos.append(frame)
        time.sleep(1)

    cam.release()
    cv2.destroyAllWindows()

    return photos
def capture_photos1():
    cam = cv2.VideoCapture(0)
    photos1 = []

    for i in range(4):

        for j in range(3,0,-1):
            ret, frame = cam.read()
            temp = frame.copy()

            cv2.putText(temp,str(j),(250,250),
                        cv2.FONT_HERSHEY_SIMPLEX,7,(255,0,0),10)

            cv2.imshow("Countdown",temp)
            cv2.waitKey(1000)

        ret, frame = cam.read()
        photos1.append(frame)
        time.sleep(1)

    cam.release()
    cv2.destroyAllWindows()

    return photos1
def capture_photos2():
    cam = cv2.VideoCapture(0)
    photos2 = []

    for i in range(3):

        for j in range(3,0,-1):
            ret, frame = cam.read()
            temp = frame.copy()

            cv2.putText(temp,str(j),(250,250),
                        cv2.FONT_HERSHEY_SIMPLEX,7,(255,0,0),10)

            cv2.imshow("Countdown",temp)
            cv2.waitKey(1000)

        ret, frame = cam.read()
        photos2.append(frame)
        time.sleep(1)

    cam.release()
    cv2.destroyAllWindows()

    return photos2
def capture_photos3():
    cam = cv2.VideoCapture(0)
    photos2 = []

    for i in range(2):

        for j in range(3,0,-1):
            ret, frame = cam.read()
            temp = frame.copy()

            cv2.putText(temp,str(j),(250,250),
                        cv2.FONT_HERSHEY_SIMPLEX,7,(255,0,0),10)

            cv2.imshow("Countdown",temp)
            cv2.waitKey(1000)

        ret, frame = cam.read()
        photos2.append(frame)
        time.sleep(1)

    cam.release()
    cv2.destroyAllWindows()

    return photos2


