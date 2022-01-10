import numpy as np
from numpy.core.numeric import zeros_like

def readFileReturnList(f):
    result = []
    while True:
        line = f.readline().replace('\n','')
        if(line == ''):
            break
        result.append(line)
    return result

def main():
    step = 10
    f = open("Day14_input", 'r')
    templete = readFileReturnList(f)[0]
    rules = readFileReturnList(f)
    f.close()
    #print(templete)
    #print(rules)
    tmp = []
    for rule in rules:
        rule = rule.split(" -> ")
        tmp.append([rule[0], rule[0][0]+rule[1]])
    rules = tmp
    #print(tmp)
    del tmp
    polymer = templete
    for s in range(step):
        #print("current step = %d"%s)
        tmp = []
        prev_frag = ''
        i = 0
        while True:
            esc = 0
            frag = polymer[i:i+1]
            if frag == '':
                tmp.append(prev_frag)
                break
            for rule in rules:
                if prev_frag+frag == rule[0]:
                    tmp.append(rule[1])
                    prev_frag = frag
                    i += 1
                    esc = 1
                    break
            if esc == 1:
                continue
            tmp.append(prev_frag)
            prev_frag = frag
            i += 1
        polymer = ''.join(tmp)
    #print(polymer)
    #print(len(polymer))
    idx = []
    cnt = []
    for c in polymer:
        if c in idx:
            cnt[idx.index(c)] += 1
        else:
            idx.append(c)
            cnt.append(1)
    print(idx)
    print(cnt)
    print(max(cnt)-min(cnt))

def lightMain():
    step = 40
    f = open("Day14_input", 'r')
    templete = readFileReturnList(f)[0]
    head = templete[0]
    tail = templete[-1]
    rules = readFileReturnList(f)
    print(rules[0][-1])
    f.close()
    elems = ['B','C','F','H','K','N','O','P','S','V']
    numElems = len(elems)
    # initialize grid
    grid = np.zeros([numElems,numElems])
    prev_t = ''
    for t in templete:
        if prev_t == '':
            prev_t = t
            continue
        #print(f"({elems.index(prev_t)}, {elems.index(t)})")
        grid[elems.index(prev_t)][elems.index(t)] += 1
        prev_t = t
    #print(grid) # initial polymer pairs
    for s in range(step):
        nextGrid = zeros_like(grid)
        for rule in rules:
            pairs = grid[elems.index(rule[0])][elems.index(rule[1])]
            nextGrid[elems.index(rule[0])][elems.index(rule[-1])] += pairs
            nextGrid[elems.index(rule[-1])][elems.index(rule[1])] += pairs
        grid = nextGrid
    print(grid)
    elemsCount = [0]*numElems
    for i in range(numElems):
        for j in range(numElems):
            elemsCount[i] += grid[i][j]
            elemsCount[j] += grid[i][j]
    elemsCount[elems.index(head)] += 1
    elemsCount[elems.index(tail)] += 1
    for i, cnt in enumerate(elemsCount):
        elemsCount[i] = cnt/2
    print(elemsCount)
    print(max(elemsCount)-min(elemsCount))


if __name__ == '__main__':
    lightMain()