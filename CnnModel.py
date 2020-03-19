from keras.engine.topology import Input
from keras.engine.training import Model
from keras.layers.convolutional import Conv2D
from keras.layers.core import Activation, Dense, Flatten
from keras.layers.merge import Add
from keras.layers.normalization import BatchNormalization
from keras.regularizers import l2
from keras.optimizers import Adam
from keras.models import Sequential, model_from_json
import os
import json

weight_path = os.path.join('.', 'model', 'model.h5')
conf_path = os.path.join('.', 'model', 'model.json')

class CnnModel:
    def __init__(self, print_summary=False):
        self.model = None
        self.print_summary = print_summary

    def build(self, H, W, D, NG):
        model = Sequential()
        model.add(Conv2D(5, (5, 5), padding='same', kernel_regularizer=l2(1e-4), input_shape=(H, W, D)))
        model.add(BatchNormalization(axis=-1))
        model.add(Activation('relu'))
        model.add(Conv2D(5, (5, 5), padding='same', kernel_regularizer=l2(1e-4)))
        model.add(BatchNormalization(axis=-1))
        model.add(Activation('relu'))
        model.add(Flatten())
        model.add(Dense(10))
        model.add(Activation('relu'))
        model.add(Dense(NG))
        model.add(Activation('softmax'))
        self.model = model

        if self.print_summary:
            self.model.summary()

    def compile(self):
        opt = Adam()
        self.model.compile(optimizer=opt,
                           loss='categorical_crossentropy',
                           metrics=['accuracy'])

    def fit(self, X, Y):
        self.model.fit(X, Y, batch_size=1)

    def load(self):
        if os.path.exists(weight_path) and os.path.exists(conf_path):
            with open(conf_path, 'r') as j:
                self.model = model_from_json(j.read())
                self.model.load_weights(weight_path)
                self.model._make_predict_function()
                return True
        else:
            print("model files does not exist at {weight_path}")
            return False

    def save(self):
        if not os.path.exists(os.path.join('.', 'model')):
            os.mkdir(os.path.join('.', 'model'))
        self.model.save_weights(weight_path)
        with open(conf_path, 'w') as f:
            f.write(self.model.to_json())

    def predict(self, x):
        return self.model.predict(x)

