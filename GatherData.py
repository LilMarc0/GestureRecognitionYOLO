import cv2 as cv
from time import time, sleep
from DataSaver import DataSaver
from Model import GestureModel
from numpy import array
from keras.utils.np_utils import to_categorical

class DataGather:
    def __init__(self, saver=None):
        self.saver = DataSaver('.\\data') or saver
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
            if show:
                cv.imshow('e2', cv.putText(f, 'gesture: ' + gesture + ' elapsed/total: ' + str(int(elapsed))
                                           + '/' + str(seconds) + ' seconds', (10, 50),
                                           cv.FONT_HERSHEY_SIMPLEX, 1, (255, 255, 255), 2))
            if cv.waitKey(5) == 27:
                break
            frames.append(f)
            sleep(1/fps)
        self.saver.save(array(frames), gesture)
        cv.destroyAllWindows()

    def load(self):
        return self.saver.load()


d = DataGather(None)
#d.record(4, 10, 'mafiot', True)
#sleep(2)
#d.record(20, 10, 'doi', True)
X, Y = d.load()
Y = to_categorical(Y, 2)
model = GestureModel()
model.build(720, 1280, 3, 2)
model.compile()
model.fit(X[:100], Y[:100])
