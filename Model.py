from keras.engine.topology import Input
from keras.engine.training import Model
from keras.layers.convolutional import Conv2D
from keras.layers.core import Activation, Dense, Flatten
from keras.layers.merge import Add
from keras.layers.normalization import BatchNormalization
from keras.regularizers import l2
from keras.optimizers import Adam
from keras.models import Sequential

class GestureModel:
    def __init__(self, print_summary=False):
        self.model = None
        self.print_summary = print_summary

    def build(self, H, W, D, NG):
        model = Sequential()
        model.add(Conv2D(20, (5, 5), padding='same', kernel_regularizer=l2(1e-4), input_shape=(H, W, D)))
        model.add(BatchNormalization(axis=-1))
        model.add(Activation('relu'))
        model.add(Conv2D(59, (5, 5), padding='same', kernel_regularizer=l2(1e-4)))
        model.add(BatchNormalization(axis=-1))
        model.add(Activation('relu'))
        model.add(Flatten())
        model.add(Dense(500))
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
