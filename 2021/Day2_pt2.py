# https://adventofcode.com/2021/day/2#part2

def main():
    f = open("Day2_input",'r')
    forward = 0
    depth = 0
    aim = 0
    while(True):
        line = f.readline()
        if(line == ''):
            break
        cmd = line.split()
        if(cmd[0] == 'forward'):
            forward += int(cmd[1])
            depth += int(cmd[1])*aim
        elif(cmd[0] == 'up'):
            aim -= int(cmd[1])
        elif(cmd[0] == 'down'):
            aim += int(cmd[1])        
    f.close()
    print("forward = %d, depth = %d, result = %d"%(forward,depth,forward*depth))

if __name__ == "__main__":
    main()