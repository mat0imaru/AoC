import numpy as np
import cv2
from utils import readFileReturnList, sign
from time import sleep

def convolution(map, filter, fx = 3, fy = 3, padding = 1, stride = 1, const_val = 0, dataType=np.int):
    (width, height) = np.shape(map)
    padded_map = np.pad(map,((padding,padding),(padding,padding)), mode='constant',constant_values = const_val)
    output = np.zeros([int((width+2*padding-fx)/stride)+1,int((height+2*padding-fy)/stride)+1], dtype=dataType)
    for i in range(0,width,stride):
        for j in range(0,height,stride):
            filter_input = padded_map[i:i+fx,j:j+fy]
            output[i][j] = filter(filter_input)
    return output

def step(map):
    return map[1][1]+1

def flash(map):
    next = map[1][1]
    if next > 9:
        return -1
    for i in range(3):
        for j in range(3):
            if (i,j) == (1,1):
                continue
            elif map[i][j] > 9:
                next += sign(next)
    return next

def disp_dumbo(octo):
    (width, height) = np.shape(octo)
    dumbo = np.zeros([width,height,3])
    colors = [
        (255,255,255),  # at 0
        (0, 0, 0),      # at 1
        (0, 0, 0),      # at 2
        (0, 0, 0),      # at 3
        (10, 0, 0),     # at 4
        (30, 21, 0),    # at 5
        (66, 46, 0),    # at 6
        (100, 70, 0),   # at 7
        (142, 100, 0),  # at 8
        (232, 162, 0)   # at 9
    ]
    for i in range(width):
        for j in range(height):
            c = octo[i][j]
            if c == 0:
                dumbo[i][j] = (255,255,255)
            else:
                dumbo[i][j] = (c**2/100*255,c**2/100*100,0)
    return dumbo/255

def main():
    total_flashes = 0
    steps = -1 # set -1 for first simultaneously flash
    lines = readFileReturnList('Day11_input')
    width = len(lines[0])
    height = len(lines)
    octopuses = np.zeros([width, height], dtype=np.int)
    for i,line in enumerate(lines):
        for j,c in enumerate(line):
            octopuses[i][j] = int(c)
    k = 0
    cv2.imshow('octopuses',cv2.resize(disp_dumbo(octopuses),dsize=(0,0), fx=100, fy=100, interpolation=cv2.INTER_LINEAR))
    cv2.waitKey(0)
    while not (k == steps):
        k = k + 1
        cv2.imshow('octopuses',cv2.resize(disp_dumbo(octopuses),dsize=(0,0), fx=100, fy=100, interpolation=cv2.INTER_LINEAR))
        key = cv2.waitKey(1)
        if key == ord('q'):
            exit()
        sleep(0.05)
        octopuses = convolution(octopuses, step)
        while np.any(octopuses > 9):
            octopuses = convolution(octopuses, flash)
        for i in range(width):
            for j in range(height):
                if octopuses[i][j] < 0:
                    octopuses[i][j] = 0
                    total_flashes += 1
        if np.all(octopuses == 0):
            print("at step %d, flash simultaneously"%k)
            if not steps > k:
                break
    cv2.imshow('octopuses',cv2.resize(disp_dumbo(octopuses),dsize=(0,0), fx=100, fy=100, interpolation=cv2.INTER_LINEAR))
    cv2.waitKey(0)
    print(total_flashes)

if __name__ == '__main__':
    main()