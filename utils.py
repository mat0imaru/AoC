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
            map[j][i] = int(line[j])
    return map

def listElemStr2Int(li):
    for idx,elem in enumerate(li):
        li[idx] = int(elem)
    return(li)

def listElemInt2Str(li):
    for idx,elem in enumerate(li):
        li[idx] = str(elem)
    return(li)

def sortString(string):
    return ''.join(sorted(string))

def subString(string1, string2):
    for c in string2:
        if c in string1:
            string1 = string1.replace(c, '')
    return string1

def sign(num) -> int: # return positive or not
    if num > 0:
        return 1
    else:
        return 0