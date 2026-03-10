import cv2

class VideoCamera:
    def __init__(self):
        # Open the webcam
        self.video = cv2.VideoCapture(0)

    def __del__(self):
        self.video.release()

    def get_frame(self):
        success, image = self.video.read()
        if not success:
            return None

        ret, jpeg = cv2.imencode('.jpg', image)
        return jpeg.tobytes()

    def capture_multiple(self, num_photos):
        photos = []
        for _ in range(num_photos):

            success, frame = self.video.read()
            if success:
                photos.append(frame)
            cv2.waitKey(500)
        return photos