import time
import cv2

class Camera:
    def __init__(self):
        # Initialize camera.
        self.vs = cv2.VideoCapture(0)

        # Let camera warm up for 5 seconds.
        print("Starting camera...")
        time.sleep(5)

        if not self.vs.isOpened():
            print("Cannot open webcam.")

    def __del__(self):
        # Clean up data.
        self.vs.release()
        cv2.destroyAllWindows()

    def get_frame(self):
        # Grab frame from video capture and return its bytes.
        frame = self.vs.read()[1]
        buf = cv2.imencode('.jpg', frame)[1].tostring()
        return buf