from utils import readFileReturnBingo, listElemStr2Int
from Bingo import Bingo
import time

def pt1():
    bingoSize = 5
    bingoList = []
    f = open('Day4_input','r')
    checkList = f.readline()
    while True:
        t = f.readline()
        if(t == "EOF"):
            break
        temp = Bingo(bingoSize)
        temp.loadBingo(readFileReturnBingo(f,bingoSize))
        bingoList.append(temp)
    f.close()
    checkList = checkList.split(',')
    checkList = listElemStr2Int(checkList)
    for num in checkList:
        for idx,bg in enumerate(bingoList):
            bg.checkBingo(num)
            if(bg.didWin() > 0):
                print("bingo")
                print(num)
                print(bg)
                return

def pt2():
    bingoSize = 5
    bingoList = []
    f = open('Day4_input','r')
    checkList = f.readline()
    while True:
        t = f.readline()
        if(t == "EOF"):
            break
        temp = Bingo(bingoSize)
        temp.loadBingo(readFileReturnBingo(f,bingoSize))
        bingoList.append(temp)
    f.close()
    checkList = checkList.split(',')
    checkList = listElemStr2Int(checkList)
    checkedList = []
    for num in checkList:
        checkedList.append(num)
        for idx,bg in enumerate(bingoList):
            if(bg.didWin() == 0):
                bg.checkBingo(num)
                if(bg.didWin() > 0):
                    print("bingo")
                    print(checkedList)
                    print(num)
                    print(bg)


if __name__ == '__main__':
    pt1()
