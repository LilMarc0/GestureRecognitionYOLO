import cv2, numpy as np
from time import sleep
from DataSaver import DataSaver
import os
from datetime import datetime

if not os.path.isdir(os.path.join('.', 'crop')):
    os.mkdir(os.path.join('.', 'crop'))

# Click on one corner of the image,
# then, click on the other corner on the image.
# The image will be cropped and saved into the folder (see below)

# Press 'esc' to quit
# Before you begin, change the path to you own video:
ds = DataSaver()
data = ds.load()

# Also, create a folder for the cropped images, and change this path to that folder:
path_to_cropped_images = './'

# mouse callback function
global click_list
global positions
positions, click_list = [], []


def callback(event, x, y, flags, param):
    if event == 1: click_list.append((x, y))
    positions.append((x, y))


cv2.namedWindow('img')
cv2.setMouseCallback('img', callback)
image_number = 0

# read first image
for i in range(len(data[0])):
    nume = data[1][i]
    img = data[0][i]
    img = np.array(img)

    if len(click_list) > 0:
        mouse_position = positions[-1]

        a = click_list[-1][0], click_list[-1][1]
        b = mouse_position[0], click_list[-1][1]
        cv2.line(img, a, b, (123, 234, 123), 3)

        a = click_list[-1][0], mouse_position[1]
        b = mouse_position[0], mouse_position[1]
        cv2.line(img, a, b, (123, 234, 123), 3)

        a = mouse_position[0], click_list[-1][1]
        b = mouse_position[0], mouse_position[1]
        cv2.line(img, a, b, (123, 234, 123), 3)

        a = click_list[-1][0], mouse_position[1]
        b = click_list[-1][0], click_list[-1][1]
        cv2.line(img, a, b, (123, 234, 123), 3)

    # If there are four points in the click list, save the image
    if len(click_list) == 2:
        # get the top left and bottom right
        a, b = click_list
        top = max(a[1], b[1])
        bottom = min(a[1], b[1])
        right = max(a[0], b[0])
        left = min(a[0], b[0])
        print(a, b, bottom, top, left, right)

        # crop out the object in the image
        crop = img[bottom: top, left: right]
        # write to the folder
        nume = './crop/' + str(datetime.now()).split()[-1]
        cv2.imwrite(nume + '.png', crop)
        print('Salvat ca ' + nume)

        # reset the click list
        click_list = []
        image_number += 1


    # try to paste the cropped image into the upper left corner
    try:
        hh, ww, xx = crop.shape
        crop_resize = cv2.resize(crop, (int(ww / 2), int(hh / 2)))
        hh, ww, xx = crop_resize.shape
        img[0:hh, 0:ww] = crop_resize
    except:
        pass

    # show the image and wait
    cv2.imshow('img', img)
    k = cv2.waitKey()
    if k == ord('a'):
        continue

cv2.destroyAllWindows()
