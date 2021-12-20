from utils import listElemStr2Int
from lanternFish import lanternFish as LF
from time import sleep

def main():
    generations = 256 # 80 for pt1, 256 for pt2
    f = open("Day6_input",'r')
    line = f.readline()
    f.close()
    fishes = line.split(',')
    fishes = listElemStr2Int(fishes)
    cnt = [0]*9
    for fish in fishes:
        cnt[fish] += 1
    fishes = cnt
    for i in range(generations):
        nextFishes = [0]*9
        print(fishes)
        for idx,fish in enumerate(fishes):
            if idx == 0:
                nextFishes[8] += fish
                nextFishes[6] += fish
            else:
                nextFishes[idx-1] += fish
        fishes = nextFishes
        sleep(0.01)
    print(sum(fishes))

if __name__ == '__main__':
    main()