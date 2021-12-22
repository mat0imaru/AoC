import numpy as np
import cv2
from utils import readFileReturnList

#Global variable
caves = []
small_caves = []
large_caves = []

def pathFinder(caves, smalls, larges, odom):
    path = []
    return path

def main():
    lines = readFileReturnList('Day12_input')
    for line in lines:
        line = line.split('-')
        for cave in line:
            if not cave in caves:
                caves.append(cave)
            if (not cave in small_caves) and cave.islower():
                small_caves.append(cave)
            if (not cave in large_caves) and cave.isupper():
                large_caves.append(cave)
    print(caves)
    print(small_caves)
    print(large_caves)
    connection = np.zeros([len(caves), len(caves)])
    for line in lines:
        line = line.split('-')
        connection[caves.index(line[0])][caves.index(line[1])] = 1
        connection[caves.index(line[1])][caves.index(line[0])] = 1
    print(connection)
    pathFinder(caves, small_caves, large_caves, ['start'])

if __name__ == '__main__':
    main()