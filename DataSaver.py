import pickle
import os
from numpy import array

class DataSaver:
    def __init__(self, path=os.path.join('.', 'data')):
        self.path = path
        if not os.path.isdir(path):
            os.mkdir(path)

    def save(self, data, gesture):
        if not os.path.isdir(os.path.join(self.path, gesture)):
            os.mkdir(os.path.join(self.path, gesture))
            workdir = os.path.join(self.path, gesture)
            lastsaved = '000'
        else:
            workdir = os.path.join(self.path, gesture)
            x = []
            for _, _, f in os.walk(workdir):
                x.extend(f)
            x.sort()
            lastsaved = x[-1][-3:]
        for idx, x in enumerate(lastsaved):
            if x.isdigit():
                lastsaved = lastsaved[idx:]
                break
        nblastsaved = int(lastsaved)
        newName = gesture + str(nblastsaved+1).zfill(3)
        with open(os.path.join(workdir, newName), 'wb+') as f:
            pickle.dump(data, f)

    def load(self):
        labels = os.listdir(self.path)
        dataset = [[], []]
        for idx, label in enumerate(labels):
            dataDir = os.path.join(self.path, label)
            pickles = []
            for _, _, f in os.walk(dataDir):
                pickles.extend(f)
            for file in pickles:
                with open(os.path.join(dataDir, file), 'rb+') as fi:
                    x = pickle.load(fi)
                    for idxp, photo in enumerate(x):
                        dataset[1].append(photo)
                        dataset[0].append(label + str(idxp))
        return array(dataset[1]), array(dataset[0])
