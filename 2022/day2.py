
#   A = rock | B = paper | C = scissor
##  X = rock | B = paper | C = scissor
##  X = lose | Y = draw  | Z = win

score = 0
f = open("day2_input", 'r')
while True:
    line = f.readline()
    if not line:
        break
    cmd = line.rstrip()
    if cmd[0] == 'A':
        if cmd[2] == 'X':
            score += 3
            print("lose")
            score += 0
        elif cmd[2] == 'Y':
            score += 1
            print("draw")
            score += 3
        elif cmd[2] == 'Z':
            score += 2
            print("win")
            score += 6
    elif cmd[0] == 'B':
        if cmd[2] == 'X':
            score += 1
            print("lose")
            score += 0
        elif cmd[2] == 'Y':
            score += 2
            print("draw")
            score += 3
        elif cmd[2] == 'Z':
            score += 3
            print("win")
            score += 6
    elif cmd[0] == 'C':
        if cmd[2] == 'X':
            score += 2
            print("lose")
            score += 0
        elif cmd[2] == 'Y':
            score += 3
            print("draw")
            score += 3
        elif cmd[2] == 'Z':
            score += 1
            print("win")
            score += 6
print(score)