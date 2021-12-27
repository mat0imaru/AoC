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
    scale = 1
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
    width += 1
    height += 1
    # initializing
    paper = np.zeros([width,height])
    for dot in dots:
        paper[dot[0]][dot[1]] = 1
    cv2.imshow("paper", cv2.resize(paper,dsize=(0,0),fx=scale,fy=scale,interpolation=cv2.INTER_NEAREST).transpose())
    cv2.waitKey(0)
    for inst in insts:
        if inst[0] == 'x':
            for i in range(width):
                for j in range(height):
                    if i > inst[1]:
                        paper[inst[1]-(i-inst[1])][j] += paper[i][j]
                        paper[i][j] = 0
        elif inst[0] == 'y':
            for i in range(width):
                for j in range(height):
                    if j > inst[1]:
                        paper[i][inst[1]-(j-inst[1])] += paper[i][j]
                        paper[i][j] = 0
        visible = 0
        for i in range(width):
            for j in range(height):
                if paper[i][j] > 0:
                    visible += 1
        print(visible)
        cv2.imshow("paper", cv2.resize(paper,dsize=(0,0),fx=scale,fy=scale,interpolation=cv2.INTER_NEAREST).transpose())
        cv2.waitKey(0)

if __name__ == '__main__':
    main()