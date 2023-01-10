import numpy as np

def readFileReturnList(filename):
    result = []
    f = open(filename,'r')
    while True:
        line = f.readline().replace('\n','')
        if(line == ''):
            break
        result.append(line)
    f.close()
    return result

def readFileReturnBingo(f,size):
    bingo = []
    for i in range(size):
        line = f.readline()
        line = line.replace('  ', ' ').lstrip()
        bingo += line.split(' ')
    bingo = listElemStr2Int(bingo)
    return bingo

def readFileReturnMap(f,width,height):    
    map = np.zeros([width,height])
    for i in range(height):
        line = f.readline()
        for j in range(width):
            map[i][j] = int(line[j])
    return map

def listElemStr2Int(li: list) -> list:
    for idx,elem in enumerate(li):
        li[idx] = int(elem)
    return(li)

def listElemInt2Str(li: list) -> list:
    for idx,elem in enumerate(li):
        li[idx] = str(elem)
    return(li)

def sortString(string: str) -> str:
    return ''.join(sorted(string))

def subString(string1: str, string2: str) -> str:
    for c in string2:
        if c in string1:
            string1 = string1.replace(c, '')
    return string1

def sign(num) -> int: # return positive or not
    if num > 0:
        return 1
    else:
        return 0

def convolution(map, filter, fx = 3, fy = 3, padding = 1, stride = 1, const_val = 0, dataType=np.int):
    (width, height) = np.shape(map)
    padded_map = np.pad(map,((padding,padding),(padding,padding)), mode='constant',constant_values = const_val)
    output = np.zeros([int((width+2*padding-fx)/stride)+1,int((height+2*padding-fy)/stride)+1], dtype=dataType)
    for i in range(0,width,stride):
        for j in range(0,height,stride):
            filter_input = padded_map[i:i+fx,j:j+fy]
            output[i][j] = filter(filter_input)
    return output