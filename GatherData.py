import cv2 as cv
from time import time, sleep
from DataSaver import DataSaver
from numpy import array
import os

class DataGather:
    def __init__(self, saver=None):
        self.saver = DataSaver(os.path.join('.', 'data')) or saver
        self.shape = (1280, 720)

    def record(self, seconds, fps, gesture, show):
        t = time()
        c = cv.VideoCapture(0)
        frames = []
        elapsed = time() - t
        while elapsed < seconds:
            elapsed = time() - t
            _, f = c.read()
            f = cv.resize(f, self.shape)
            fc = f.copy()
            if show:
                cv.imshow('e2', cv.putText(f, 'gesture: ' + gesture + ' elapsed/total: ' + str(int(elapsed))
                                           + '/' + str(seconds) + ' seconds', (10, 50),
                                           cv.FONT_HERSHEY_SIMPLEX, 1, (255, 255, 255), 2))
            if cv.waitKey(5) == 27:
                break
            frames.append(fc)
            sleep(1/fps)
        self.saver.save(array(frames), gesture)
        cv.destroyAllWindows()

    def load(self):
        return self.saver.load()
