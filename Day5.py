import numpy as np
from utils import readFileReturnList, listElemStr2Int
import time
import cv2

def main():
    width = 1000
    height = 1000

    field = np.zeros([width,height])
    img = np.zeros([width,height,3])
    for i in range(width):
        for j in range(height):
            if field[i][j] == 0:
                img[i][j] = (0,0,0)
            elif field[i][j] == 1:
                img[i][j] = (0,255,0)
            else:
                img[i][j] = (0,0,255)
    #lines = readFileReturnList("Day5_input_sample")
    lines = readFileReturnList("Day5_input")
    
    for line in lines:
        line = line.replace(' -> ',',')
        line = line.split(',')
        line = listElemStr2Int(line)
        #print(line)
        xdiff = line[2] - line[0]
        ydiff = line[3] - line[1]
        if xdiff != 0:
            grad = ydiff/xdiff
        else:
            grad = 'inf'
        if(line[0] == line[2]): # x1 == x2
            if(line[1] > line[3]):
                for i in range(line[3],line[1]+1):
                    field[line[0]][i] += 1
            else:
                for i in range(line[1],line[3]+1):
                    field[line[0]][i] += 1
        elif(line[1] == line[3]): # y1 == y2
            if(line[0] > line[2]):
                for i in range(line[2],line[0]+1):
                    field[i][line[1]] += 1
            else:
                for i in range(line[0],line[2]+1):
                    field[i][line[1]] += 1
        #### below condition for part 2 ####
        # +45deg
        elif( (abs(xdiff) == abs(ydiff))
            & (grad < 0) ):
            diff = abs(xdiff)
            #print(line)
            #print(diff)
            for i in range(diff+1):
                field[min(line[0],line[2])+i][max(line[1],line[3])-i] += 1
        # -45deg
        elif( (abs(xdiff) == abs(ydiff))
            & (grad > 0) ):
            diff = abs(xdiff)
            #print(line)
            #print(diff)
            for i in range(diff+1):
                field[min(line[0],line[2])+i][min(line[1],line[3])+i] += 1
        #print(field.transpose())

    print("size of field = (%d, %d)"%(width,height))
    result = 0
    img = np.zeros([width,height,3])
    field = field.transpose()
    for i in range(width):
        for j in range(height):
            if field[i][j] == 0:
                img[i][j] = (0,0,0)
                if i%2 == 0:
                    img[i][j] += (30,30,30)
                if j%2 == 0:
                    img[i][j] += (30,30,30)     
            elif field[i][j] == 1:
                img[i][j] = (0,250,50)
            elif field[i][j] == 2:
                img[i][j] = (0,100,150)
                result += 1
            else:
                img[i][j] = (0,50,250)
                result += 1
    img = img/255
    print(result)
    #img = cv2.resize(img, dsize=(0,0), fx=20, fy=20, interpolation=cv2.INTER_NEAREST)
    #img = cv2.resize(img, dsize=(0,0), fx=0.5, fy=0.5, interpolation=cv2.INTER_LINEAR)
    cv2.imshow('field', img)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
    exit()


if __name__ == "__main__":
    main()