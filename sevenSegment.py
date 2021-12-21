import numpy as np
from cv2 import imshow, waitKey, line, circle

class wiring:
    def __init__(self):
        self.zero = 'abcefg'
        self.one = 'cf'
        self.two = 'acdeg'
        self.three = 'acdfg'
        self.four = 'bcdf'
        self.five = 'abdfg'
        self.six = 'abdefg'
        self.seven = 'acf'
        self.eight = 'abcdefg'
        self.nine = 'abcdfg'
    def set(self,num,sequence):
        sequence = ''.join(sorted(sequence))
        if num == 0:
            self.zero = sequence
        elif num == 1:
            self.one = sequence
        elif num == 2:
            self.two = sequence
        elif num == 3:
            self.three = sequence
        elif num == 4:
            self.four = sequence
        elif num == 5:
            self.five = sequence
        elif num == 6:
            self.six = sequence
        elif num == 7:
            self.seven = sequence
        elif num == 8:
            self.eight = sequence
        elif num == 9:
            self.nine = sequence
    def encode(self, num) -> str:
        if num == 0:
            return self.zero
        elif num == 1:
            return self.one
        elif num == 2:
            return self.two
        elif num == 3:
            return self.three
        elif num == 4:
            return self.four
        elif num == 5:
            return self.five
        elif num == 6:
            return self.six
        elif num == 7:
            return self.seven
        elif num == 8:
            return self.eight
        elif num == 9:
            return self.nine
    def decode(self, sequence) -> int:
        sequence = ''.join(sorted(sequence))
        if sequence == self.zero:
            return 0
        elif sequence == self.one:
            return 1
        elif sequence == self.two:
            return 2
        elif sequence == self.three:
            return 3
        elif sequence == self.four:
            return 4
        elif sequence == self.five:
            return 5
        elif sequence == self.six:
            return 6
        elif sequence == self.seven:
            return 7
        elif sequence == self.eight:
            return 8
        elif sequence == self.nine:
            return 9
    def clear(self):
        self.zero = 'abcefg'
        self.one = 'cf'
        self.two = 'acdeg'
        self.three = 'acdfg'
        self.four = 'bcdf'
        self.five = 'abdfg'
        self.six = 'abdefg'
        self.seven = 'acf'
        self.eight = 'abcdefg'
        self.nine = 'abcdfg'

class Display:
    def __init__(self):
        self.img = np.zeros([160,1400,3])
        self.windowName = 'Display'
        self.numbers = ['']*14
        self.show(self.numbers)
    def show(self, li, color = (0,0,255)):
        self.numbers = li
        self.img = np.zeros([160,1400,3])
        self.img = circle(self.img, (1000,60), 5, color, -1)
        self.img = circle(self.img, (1000,100), 5, color, -1)
        for idx, number in enumerate(self.numbers):
            if 'a' in number:
                self.img = line(self.img, (100*idx+30,20), (100*idx+70,20), color, 10)
            if 'b' in number:
                self.img = line(self.img, (100*idx+20,30), (100*idx+20,70), color, 10)
            if 'c' in number:
                self.img = line(self.img, (100*idx+80,30), (100*idx+80,70), color, 10)
            if 'd' in number:
                self.img = line(self.img, (100*idx+30,80), (100*idx+70,80), color, 10)
            if 'e' in number:
                self.img = line(self.img, (100*idx+20,90), (100*idx+20,130), color, 10)
            if 'f' in number:
                self.img = line(self.img, (100*idx+80,90), (100*idx+80,130), color, 10)
            if 'g' in number:
                self.img = line(self.img, (100*idx+30,140), (100*idx+70,140), color, 10)
        imshow(self.windowName,self.img)
        waitKey(1)
    def clear(self):
        self.numbers = ['']*14
        self.show(self.numbers)