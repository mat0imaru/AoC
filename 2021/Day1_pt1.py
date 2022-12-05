# https://adventofcode.com/2021/day/1#part1

def main():
    f = open("Day1_input", 'r')
    inc_count = 0
    i = 0
    value = int(f.readline())
    prev_value = value
    while(value):
        diff = value - prev_value
        print("prev_value = %d, value = %d, diff = %d"%(prev_value,value,diff))
        if(diff > 0):
            inc_count += 1
        try:        
            prev_value = value
            value = int(f.readline())
        except:
            break
    print(inc_count)
    f.close()


if __name__ == "__main__":
    main()