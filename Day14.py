from os import read, rename


def readFileReturnList(f):
    result = []
    while True:
        line = f.readline().replace('\n','')
        if(line == ''):
            break
        result.append(line)
    return result

def main():
    step = 40
    f = open("Day14_input", 'r')
    templete = readFileReturnList(f)[0]
    rules = readFileReturnList(f)
    f.close()
    print(templete)
    print(rules)
    tmp = []
    for rule in rules:
        rule = rule.split(" -> ")
        tmp.append([rule[0], rule[0][0]+rule[1]])
    rules = tmp
    print(tmp)
    del tmp
    polymer = templete
    for s in range(step):
        print("current step = %d"%s)
        tmp = []
        prev_frag = ''
        i = 0
        while True:
            esc = 0
            frag = polymer[i:i+1]
            if frag == '':
                tmp.append(prev_frag)
                break
            for rule in rules:
                if prev_frag+frag == rule[0]:
                    tmp.append(rule[1])
                    prev_frag = frag
                    i += 1
                    esc = 1
                    break
            if esc == 1:
                continue
            tmp.append(prev_frag)
            prev_frag = frag
            i += 1
        polymer = ''.join(tmp)
    print(polymer)
    print(len(polymer))
    idx = []
    cnt = []
    for c in polymer:
        if c in idx:
            cnt[idx.index(c)] += 1
        else:
            idx.append(c)
            cnt.append(1)
    print(idx)
    print(cnt)
    print(max(cnt)-min(cnt))


if __name__ == '__main__':
    main()