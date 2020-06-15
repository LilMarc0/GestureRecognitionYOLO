import pickle
import os
import numpy as np
from PIL import Image


if not os.path.isdir('gramada'):
    os.mkdir('gramada')
dataDir = os.path.join('.', 'data')
fisiere = os.listdir(dataDir)

i = 0
for fisier in fisiere:
    pickles = []
    for _, _, f in os.walk(dataDir):
        pickles.extend(f)
    for picklef in pickles:
        with open(os.path.join(dataDir, fisier, picklef), 'rb+') as fi:
            x = pickle.load(fi)
            for photo in x:
                im = Image.fromarray(photo)
                b, g, r = im.split()
                im = Image.merge("RGB", (r, g, b))
                im.save("./gramada/gramada_{}.jpeg".format(i))
                i += 1
