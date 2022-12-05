# https://adventofcode.com/2021/day/3#part1
from utils import readFileReturnList

def main():
    inputs = readFileReturnList("Day3_input")
    OG = inputs
    CS = inputs
    for i in range(len(OG[0])):
        count = 0
        for _, og in enumerate(OG):
            if(og[i] == '1'):
                count += 1
        depth = len(OG)
        if(count/depth >= 0.5):
            MSB = 1
        else:
            MSB = 0
        tmp = []
        for _, og in enumerate(OG):
            if(og[i] == str(MSB)):
                tmp.append(og)
        OG = tmp
        if(len(OG) == 1):
            break
    for i in range(len(CS[0])):
        count = 0
        for _, cs in enumerate(CS):
            if(cs[i] == '1'):
                count += 1
        depth = len(CS)
        if(count/depth >= 0.5):
            MSB = 0
        else:
            MSB = 1
        tmp = []
        for _, cs in enumerate(CS):
            if(cs[i] == str(MSB)):
                tmp.append(cs)
        CS = tmp
        if(len(CS) == 1):
            break
    OG = eval('0b'+OG.pop())
    CS = eval('0b'+CS.pop())
    print(OG*CS)
    
if __name__ == "__main__":
    main()