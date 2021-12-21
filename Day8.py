from time import sleep
from utils import readFileReturnList, subString, listElemInt2Str
from sevenSegment import Display, wiring

def solve(line) -> wiring:
    wir = wiring()
    tmp = []
    for number in line:
        number = ''.join(sorted(number))
        if(len(number) == 2):
            wir.set(1, number)
            one = number
        elif(len(number) == 3):
            wir.set(7, number)
        elif(len(number) == 4):
            wir.set(4, number)
            four = number
        elif(len(number) == 7):
            wir.set(8, number)
        else:
            tmp.append(number)
    for number in tmp:
        l = len(number)
        s1 = len(subString(number,one))
        s4 = len(subString(number,four))
        if s1 == 3:
            wir.set(3, number)
        elif s1 == 5:
            wir.set(6, number)
        else:
            if s4 == 3:
                if l == 6:
                    wir.set(0,number)
                elif l == 5:
                    wir.set(2, number)
            elif s4 == 2:
                if l == 6:
                    wir.set(9, number)
                elif l == 5:
                    wir.set(5, number)
    return wir

def main():
    lines = readFileReturnList("Day8_input")
    disp = Display()
    normal = wiring()
    result = 0
    total = 0
    delay = 0
    for line in lines:
        line = line.replace('| ', '')
        line = line.split(' ')
        disp.show(line)
        sleep(0.5*delay)
        w = solve(line)
        tmp = []
        decoded = []
        for number in line:
            i = w.decode(number)
            decoded.append(i)
            s = normal.encode(i)
            tmp.append(s)
        line = tmp
        for number in line[-4:]:
            if len(number) in [2,4,3,7]:
                result += 1
        decoded = listElemInt2Str(decoded)
        total += int(''.join(decoded[-4:]))
        disp.show(line,(0,255,0))
        sleep(1*delay)
    print(result) #pt1
    print(total) #pt2

if __name__ == '__main__':
    main()