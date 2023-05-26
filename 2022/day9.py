# --- Day 9: Rope Bridge ---
# This rope bridge creaks as you walk along it. You aren't sure how old it is, or whether it can even support your weight.
# It seems to support the Elves just fine, though. The bridge spans a gorge which was carved out by the massive river far below you.
# You step carefully; as you do, the ropes stretch and twist. You decide to distract yourself by modeling rope physics; maybe you can even figure out where not to step.
# Consider a rope with a knot at each end; these knots mark the head and the tail of the rope. If the head moves far enough away from the tail, the tail is pulled toward the head.
# Due to nebulous reasoning involving Planck lengths, you should be able to model the positions of the knots on a two-dimensional grid. Then, by following a hypothetical series of motions (your puzzle input) for the head, you can determine how the tail will move.
# Due to the aforementioned Planck lengths, the rope must be quite short; in fact, the head (H) and tail (T) must always be touching (diagonally adjacent and even overlapping both count as touching):

# ....
# .TH.
# ....

# ....
# .H..
# ..T.
# ....

# ...
# .H. (H covers T)
# ...
# If the head is ever two steps directly up, down, left, or right from the tail, the tail must also move one step in that direction so it remains close enough:

# .....    .....    .....
# .TH.. -> .T.H. -> ..TH.
# .....    .....    .....

# ...    ...    ...
# .T.    .T.    ...
# .H. -> ... -> .T.
# ...    .H.    .H.
# ...    ...    ...
# Otherwise, if the head and tail aren't touching and aren't in the same row or column, the tail always moves one step diagonally to keep up:

# .....    .....    .....
# .....    ..H..    ..H..
# ..H.. -> ..... -> ..T..
# .T...    .T...    .....
# .....    .....    .....

# .....    .....    .....
# .....    .....    .....
# ..H.. -> ...H. -> ..TH.
# .T...    .T...    .....
# .....    .....    .....
# You just need to work out where the tail goes as the head follows a series of motions. Assume the head and the tail both start at the same position, overlapping.

# For example:

# R 4
# U 4
# L 3
# D 1
# R 4
# D 1
# L 5
# R 2
# This series of motions moves the head right four steps, then up four steps, then left three steps, then down one step, and so on. After each step, you'll need to update the position of the tail if the step means the head is no longer adjacent to the tail. Visually, these motions occur as follows (s marks the starting position as a reference point):

# == Initial State ==

# ......
# ......
# ......
# ......
# H.....  (H covers T, s)

# == R 4 ==

# ......
# ......
# ......
# ......
# TH....  (T covers s)

# ......
# ......
# ......
# ......
# sTH...

# ......
# ......
# ......
# ......
# s.TH..

# ......
# ......
# ......
# ......
# s..TH.

# == U 4 ==

# ......
# ......
# ......
# ....H.
# s..T..

# ......
# ......
# ....H.
# ....T.
# s.....

# ......
# ....H.
# ....T.
# ......
# s.....

# ....H.
# ....T.
# ......
# ......
# s.....

# == L 3 ==

# ...H..
# ....T.
# ......
# ......
# s.....

# ..HT..
# ......
# ......
# ......
# s.....

# .HT...
# ......
# ......
# ......
# s.....

# == D 1 ==

# ..T...
# .H....
# ......
# ......
# s.....

# == R 4 ==

# ..T...
# ..H...
# ......
# ......
# s.....

# ..T...
# ...H..
# ......
# ......
# s.....

# ......
# ...TH.
# ......
# ......
# s.....

# ......
# ....TH
# ......
# ......
# s.....

# == D 1 ==

# ......
# ....T.
# .....H
# ......
# s.....

# == L 5 ==

# ......
# ....T.
# ....H.
# ......
# s.....

# ......
# ....T.
# ...H..
# ......
# s.....

# ......
# ......
# ..HT..
# ......
# s.....

# ......
# ......
# .HT...
# ......
# s.....

# ......
# ......
# HT....
# ......
# s.....

# == R 2 ==

# ......
# ......
# .H....  (H covers T)
# ......
# s.....

# ......
# ......
# .TH...
# ......
# s.....
# After simulating the rope, you can count up all of the positions the tail visited at least once. In this diagram, s again marks the starting position (which the tail also visited) and # marks other positions the tail visited:

# ..##..
# ...##.
# .####.
# ....#.
# s###..
# So, there are 13 positions the tail visited at least once.

# Simulate your complete hypothetical series of motions. How many positions does the tail of the rope visit at least once?

import math


class Point:
    def __init__(self, ix=0, iy=0) -> None:
        self.x = ix
        self.y = iy
    # differece between two points

    def diff(self, other):
        ret = Point()
        ret.x = self.x - other.x
        ret.y = self.y - other.y
        return ret
    # add two points

    def add(self, other):
        ret = Point()
        ret.x = self.x + other.x
        ret.y = self.y + other.y
        return ret
    # multiply a point by a scalar

    def mult(self, s):
        ret = Point()
        ret.x = self.x * s
        ret.y = self.y * s
        return ret
    # divide a point by a scalar

    def div(self, s):
        ret = Point()
        ret.x = self.x / s
        ret.y = self.y / s
        return ret
    # find max magnitude among x and y

    def maxmag(self):
        return max(abs(self.x), abs(self.y))
    # apply celling to x and y

    def ceil(self):
        ret = Point()
        ret.x = math.ceil(self.x)
        ret.y = math.ceil(self.y)
        return ret
    # apply floor to x and y

    def floor(self):
        ret = Point()
        ret.x = math.floor(self.x)
        ret.y = math.floor(self.y)
        return ret
    # qunatize x and y

    def quant(self):
        ret = Point()
        if abs(self.x) < 0.1:
            ret.x = 0
        if abs(self.y) < 0.1:
            ret.y = 0
        if self.x >= 0.1:
            ret.x = math.ceil(self.x)
        elif self.x <= -0.1:
            ret.x = math.floor(self.x)
        if self.y >= 0.1:
            ret.y = math.ceil(self.y)
        elif self.y <= -0.1:
            ret.y = math.floor(self.y)
        return ret

    def __repr__(self) -> str:
        return f"({self.x},{self.y})"


def distance(a, b):
    return (abs(a.x-b.x)**2 + abs(a.y-b.y)**2)**0.5


def ropeDynamics(Head, Tail):
    if distance(Head, Tail) > 1.5:
        # calculate differece
        d = Head.diff(Tail)
        # scaling to prohibit jumping
        d = d.div(d.maxmag())
        # quantize vector
        d = d.quant()
        Tail = Tail.add(d)
    nextTail = Tail
    return nextTail


def main_1():
    # loading input
    cmds = []
    with open('day9_input', 'r') as f:
        for line in f:
            cmds.append(line.strip())
    # print(cmds)
    # processing cmds
    tmp = []
    for cmd in cmds:
        cmd = cmd.split(' ')
        cmd[1] = int(cmd[1])
        tmp.append(cmd)
    cmds = tmp
    # print(cmds)
    # initial conditions
    Head = Point()
    Tail = Point()
    reached = set()
    for cmd in cmds:
        print(cmd)
        for i in range(cmd[1]):
            # update Head according to command
            if cmd[0] == "U":
                Head.y += 1
            elif cmd[0] == "D":
                Head.y -= 1
            elif cmd[0] == "L":
                Head.x -= 1
            elif cmd[0] == "R":
                Head.x += 1
            # update Tail according to dynamics
            print(
                f"Head: {Head}, Tail: {Tail}, distance: {distance(Head, Tail)}")
            Tail = ropeDynamics(Head, Tail)
            # add Tail to reached
            reached.add((Tail.x, Tail.y))
    print(len(reached))


def main_2():
    # loading input
    cmds = []
    with open('day9_input', 'r') as f:
        for line in f:
            cmds.append(line.strip())
    # print(cmds)

    # processing cmds
    tmp = []
    for cmd in cmds:
        cmd = cmd.split(' ')
        cmd[1] = int(cmd[1])
        tmp.append(cmd)
    cmds = tmp
    # print(cmds)
    testcmds = [['R', 5],
            ['U', 8],
            ['L', 8],
            ['D', 3],
            ['R', 17],
            ['D', 10],
            ['L', 25],
            ['U', 20],]
    # initial conditions
    Head = Point()
    numKnots = 9
    knots = []
    for i in range(numKnots):
        knots.append(Point())
    reached = set()
    # simulate rope
    for cmd in cmds:
        print(cmd)
        for i in range(cmd[1]):
            # update Head according to command
            if cmd[0] == "U":
                Head.y += 1
            elif cmd[0] == "D":
                Head.y -= 1
            elif cmd[0] == "L":
                Head.x -= 1
            elif cmd[0] == "R":
                Head.x += 1
            # update Tail according to dynamics
            # print(f"Head: {Head}, Tail: {Tail}, distance: {distance(Head, Tail)}")
            knots[0] = ropeDynamics(Head, knots[0])
            for i in range(numKnots-1):
                knots[i+1] = ropeDynamics(knots[i], knots[i+1])
            print(f"{Head}, {knots[0]}, {knots[1]}, {knots[2]}, {knots[3]}, {knots[4]}, {knots[5]}, {knots[6]}, {knots[7]}, {knots[8]}")
            Tail = knots[-1]
            # add Tail to reached
            reached.add((Tail.x, Tail.y))
    print(len(reached))


if __name__ == "__main__":
    main_2()
