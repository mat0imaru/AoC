def pt1():
    init_state = []
    commands = []
    with open("day5_input", 'r') as f:
        while True:
            line = f.readline().strip("\n")
            if not line:
                break
            init_state.append(line)
        while True:
            command = f.readline().strip("\n")
            if not command:
                break
            command = command.split(' ')
            command = [int(command[1]),int(command[3]),int(command[5])]
            commands.append(command)
    ship = [[],[],[],[],[],[],[],[],[]]
    for line in init_state:
        line = line.replace('[','').replace(']','').replace("    ", "*").replace(" ", '')
        for i, c in enumerate(line):
            if c != '*':
                ship[i].append(c)
    for s in ship:
        s.pop()
        s.reverse()
    # print(ship)
    # print(commands)
    for cmd in commands:
        for i in range(cmd[0]):
            ship[cmd[2]-1].append(ship[cmd[1]-1].pop())
    print(ship)
    for s in ship:
        print(s[-1])

def pt2():
    init_state = []
    commands = []
    with open("day5_input", 'r') as f:
        while True:
            line = f.readline().strip("\n")
            if not line:
                break
            init_state.append(line)
        while True:
            command = f.readline().strip("\n")
            if not command:
                break
            command = command.split(' ')
            command = [int(command[1]),int(command[3]),int(command[5])]
            commands.append(command)
    ship = [[],[],[],[],[],[],[],[],[]]
    for line in init_state:
        line = line.replace('[','').replace(']','').replace("    ", "*").replace(" ", '')
        for i, c in enumerate(line):
            if c != '*':
                ship[i].append(c)
    for s in ship:
        s.pop()
        s.reverse()
    # print(ship)
    # print(commands)
    for cmd in commands:
        tmp = []
        for i in range(cmd[0]):
            tmp.append(ship[cmd[1]-1].pop())
        tmp.reverse()
        ship[cmd[2]-1] = ship[cmd[2]-1] + tmp
        tmp = []
    print(ship)
    for s in ship:
        print(s[-1])

if __name__ == "__main__":
    pt2()
