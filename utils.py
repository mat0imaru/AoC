import time

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

def listElemStr2Int(li):
    for idx,elem in enumerate(li):
        li[idx] = int(elem)
    return(li)
