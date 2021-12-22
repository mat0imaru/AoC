import numpy as np
import cv2
from utils import readFileReturnList
from time import sleep
#Global variable
caves = []
small_caves = []
large_caves = []
sz = 0

def pathFinder(odom, adjMat, paths, validation):
    odometry = odom
    tail = odometry[-1]
    i = caves.index(tail)
    for j in range(sz):
        if adjMat[i][j] == 1:
            next = caves[j]
            next_odom = odometry + next.split()
            print(next_odom)
            if validation(next_odom) and next =='end':
                print("found one!")
                paths.append(next_odom)
                return [next_odom]
            elif validation(next_odom):
                pathFinder(next_odom, adjMat, paths, validation)

def vaildOdom1(odom):
    for i,o in enumerate(odom):
        if (o in small_caves) and (o in odom[:i]):
            return False
    return True

def vaildOdom2(odom):
    visited = []
    for i,o in enumerate(odom):
        if (o in small_caves) and (o in odom[:i]):
            if (o != 'start') and (o != 'end'):
                if len(visited) == 0:
                    visited.append(o)
                else:
                    return False
            else:
                return False
    return True


def main():
    global sz
    lines = readFileReturnList('Day12_input')
    for line in lines:
        line = line.split('-')
        for cave in line:
            if not cave in caves:
                if (cave == 'start')or(cave == 'end'):
                    pass
                else:
                    caves.append(cave)
            if (not cave in small_caves) and cave.islower():
                small_caves.append(cave)
            if (not cave in large_caves) and cave.isupper():
                large_caves.append(cave)
    caves.insert(0,'start')
    caves.append('end')
    sz = len(caves)
    print(caves)
    print(small_caves)
    print(large_caves)
    adj_mat = np.zeros([sz, sz])
    for line in lines:
        line = line.split('-')
        adj_mat[caves.index(line[0])][caves.index(line[1])] = 1
        adj_mat[caves.index(line[1])][caves.index(line[0])] = 1
    print(adj_mat)
    paths = []
    pathFinder(['start'], adj_mat, paths, vaildOdom2)
    print(len(paths))

if __name__ == '__main__':
    main()