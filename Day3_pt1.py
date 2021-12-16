# https://adventofcode.com/2021/day/3#part1
from os import read
from utils import readFileReturnList

def main():
    inputs = readFileReturnList("Day3_input")
    length = len(inputs[0])
    depth = len(inputs)
    gamma = []
    for i in range(length):
        count = 0
        for j in range(depth):
            if(inputs[j][i] == '1'):
                count += 1
        if(count/depth > 0.5):
            gamma.append('1')
        else:
            gamma.append('0')
    gamma = str(gamma).replace('\'','').replace('[','').replace(']','').replace(',','').replace(' ','')
    gamma_rate = eval('0b'+gamma)
    epsilon_rate = 0xFFF ^ gamma_rate
    print(gamma_rate*epsilon_rate)


if __name__ == "__main__":
    main()