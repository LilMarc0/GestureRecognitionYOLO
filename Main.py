from GatherData import *
from DataSaver import *
import argparse
import numpy as np
import cv2 as cv
import time

'''
    Pumn - perlin noise
    Artificii - 1deget
    Ok - pendul
    Palma - Boids
    2degete - boids
    like - fluide
'''

gestures = ['palma', 'ok', 'like', '1deget', '2deget', 'pumn']

def create_parser():
    parser = argparse.ArgumentParser()
    parser.add_argument("--gest", help="Numele gestului", choices=gestures)
    parser.add_argument("--show", help="Daca vreti sa va vedeti", type=bool, default=True)
    parser.add_argument("--secs", help="Cate secunde va inregistrati", type=int, default=20)
    parser.add_argument("--fps", help="Cate cadre pe secunda", type=int, default=15)
    return parser


if __name__ == '__main__':
    parser = create_parser()
    args = parser.parse_args()
    saver = DataSaver()
    recorder = DataGather(saver)
    recorder.record(args.secs, args.fps, args.gest, args.show)

