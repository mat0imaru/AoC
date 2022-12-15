def main():
    line = ''
    with open("day6_input") as f:
        line = f.readline().rstrip()
    for i in range(14, len(line)):
        buffer = line[i-14:i]
        if len(set(buffer)) == 14:
            print(i)
            # print(len(set(buffer)))
            break

if __name__ == "__main__":
    main()