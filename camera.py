from imutils.video.pivideostream import PiVideoStream
import time
import cv2


class Camera:
    def __init__(self):
        self.vs = PiVideoStream().start()
        self.detections = 0

        # Let camera warm up for 5 seconds.
        print("Starting camera...")
        time.sleep(5)

    def __del__(self):
        self.vs.stop()
        cv2.destroyAllWindows()

    def get_frame(self):
        readFrame = self.vs.read()

        # Return bytes of frame.
        buf = cv2.imencode('.jpg', readFrame)[1].tostring()
        return buf