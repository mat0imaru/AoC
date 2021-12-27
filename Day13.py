import cv2
import numpy as np

def readFileReturnList(f):
    result = []
    while True:
        line = f.readline().replace('\n','')
        if(line == ''):
            break
        result.append(line)
    return result

def main():
    # data loading
    f = open("Day13_input",'r')
    dots = readFileReturnList(f)
    insts = readFileReturnList(f)
    f.close()
    # data processing
    tmp = []
    width = 0
    height = 0
    for dot in dots:
        dot = dot.split(',')
        dot = [int(dot[0]), int(dot[1])]
        width = max(width, dot[0])
        height = max(height, dot[1])
        tmp.append(dot)
    dots = tmp
    tmp = []
    for inst in insts:
        dir = inst.split('=')[0][-1]
        foldLine = int(inst.split('=')[1])
        tmp.append([dir,foldLine])
    insts = tmp
    del tmp
    print(dots)
    print(insts)
    print("width = %d, height = %d"%(width,height))
    # initializing
    paper = np.zeros([width+1,height+1])
    for dot in dots:
        paper[dot[0]][dot[1]] = 1
    cv2.imshow("paper", paper)
    cv2.waitKey(0)
    for inst in insts:
        pass
    cv2.imshow("paper", paper)
    cv2.waitKey(0)
    

if __name__ == '__main__':
    main()