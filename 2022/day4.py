import numpy as np

def parse_line(line:str):
    ret = []
    A, B = line.split(',')
    ret = A.split('-') + B.split('-')
    for i, r in enumerate(ret):
        ret[i] = int(r)
    return ret

def main():
    contain_count = 0
    overlap_count = 0
    with open("day4_input", 'r') as f:
        while True:
            line = f.readline().strip()
            if not line:
                break
            parsed = parse_line(line)
            A = set()
            for i in range(parsed[0], parsed[1]+1):
                A.add(i)
            B = set()
            for j in range(parsed[2], parsed[3]+1):
                B.add(j)
            if A&B == A:
                print(f"{parsed[2]}-{parsed[3]} fully contains {parsed[0]}-{parsed[1]}")
                contain_count += 1
            elif A&B == B:
                print(f"{parsed[0]}-{parsed[1]} fully contains {parsed[2]}-{parsed[3]}")
                contain_count += 1
            if len(A&B) > 0:
                print(f"{parsed[0]}-{parsed[1]} & {parsed[2]}-{parsed[3]} overlaps")
                overlap_count += 1
    print(f"{contain_count} pairs are contain one another")
    print(f"{overlap_count} pairs are overlapping")


if __name__ == "__main__":
    main()