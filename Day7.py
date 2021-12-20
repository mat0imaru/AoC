from utils import listElemStr2Int
from matplotlib import pyplot as ppt

def main():
    f = open("Day7_input",'r')
    line = f.readline()
    f.close()
    h_pos = line.split(',')
    h_pos = listElemStr2Int(h_pos)
    print(h_pos)
    cost_list = []
    for i in range(max(h_pos)):
        cost = 0
        for crab in h_pos:
            cost += abs(crab - i)   # for pt1
            #cost += (abs(crab - i)*(abs(crab - i)+1))/2 # for pt2
        cost_list.append(cost)
    print(cost_list)
    ppt.plot(cost_list)
    ppt.show()
    print(min(cost_list))
if __name__ == "__main__":
    main()