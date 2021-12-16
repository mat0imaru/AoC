import numpy as np
from utils import readFileReturnList, listElemStr2Int
import time

def main():
    maX = 0
    prev_maX = 0
    maY = 0
    prev_maY = 0
    resizeFlag = 0
    field = np.zeros([maX,maY])
    lines = readFileReturnList("Day5_input")
    for line in lines:
        line = line.replace(' -> ',',')
        line = line.split(',')
        line = listElemStr2Int(line)
        print(line)
        prev_maX = maX
        prev_maY = maY
        if(line[0] > maX):
            maX = line[0]
            resizeFlag = 1
        if(line[1] > maY):
            maY = line[1]
            resizeFlag = 1
        if(line[2] > maX):
            maX = line[2]
            resizeFlag = 1
        if(line[3] > maY):
            maY = line[3]
            resizeFlag = 1
        if(resizeFlag == 1):
            resizeFlag = 0
            new_field = np.zeros([maX,maY])
            print(np.shape(new_field))
            for i in range(prev_maX):
                for j in range(prev_maY):
                    new_field[i][j] = field[i][j]
            field = new_field
        print(np.shape(field))
        if(line[0] == line[2]): # x1 == x2
            for i in range(line[1],line[3]):
                field[line[0]][i] += 1
        if(line[1] == line[3]): # y1 == y2
            for i in range(line[0],line[2]):
                field[i][line[1]] += 1
        print(field)
        time.sleep(100)


if __name__ == "__main__":
    main()