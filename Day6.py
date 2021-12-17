from utils import listElemStr2Int
from lanternFish import lanternFish as LF

def main():
    generations = 256
    f = open("Day6_input",'r')
    line = f.readline()
    f.close()
    fishes = line.split(',')
    fishes = listElemStr2Int(fishes)
    nextFishes = []
    for i in range(generations):
        for fish in fishes:
            if fish == 0:
                nextFishes.append(6)
                nextFishes.append(8)
            else:
                nextFishes.append(fish-1)
        fishes = nextFishes
        nextFishes = []
        print("Gen %d, fishes = %d"%(i+1,len(fishes)))
    

if __name__ == '__main__':
    main()