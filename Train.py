from Model import *
from DataSaver import *
from keras.utils import to_categorical
import numpy as np

if __name__ == '__main__':
    d = DataSaver()
    X, Y = d.load()
    Y = to_categorical(Y)
    model = GestureModel()
    model.build(720, 1280, 3, Y.shape[-1])
    model.compile()
    model.fit(X[:2], Y[:2])
    model.save()
    model.load()
    model.compile()
    print(model.predict(np.array(X[1]).reshape((-1, 720, 1280, 3))))