# https://adventofcode.com/2021/day/1#part2

def main():
    f = open("Day1_input", 'r')
    list = []
    while(True):
        value = f.readline()
        if value == '':
            break
        list.append(int(value))
    f.close()
    p_ts = 9999999
    inc_count = 0
    for i in range(len(list)-2):
        ts = sum(list[i:i+3])
        diff = ts - p_ts
        print("prev_ts = %d, ts = %d, diff = %d"%(p_ts,ts, diff))
        if(diff > 0):
            inc_count += 1
        p_ts = ts
    print(inc_count)

if __name__ == "__main__":
    main()