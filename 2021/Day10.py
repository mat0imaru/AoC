from utils import readFileReturnList

def main():
    incompletes = 0
    corrupted = 0
    total_syntax_error_score = 0
    opens = ['(', '[', '{', '<']
    closes = [')', ']', '}', '>']
    corrupted_error_score = [3,57,1197,25137]
    incomplete_lines = []
    incompletes_correction_scores = []
    lines = readFileReturnList('Day10_input')
    for line in lines:
        tmp = []
        prev_corrupted = corrupted
        for c in line:
            if c in opens:
                tmp.append(c)
            if c in closes:
                t = tmp.pop()
                if closes.index(c) != opens.index(t):
                    corrupted += 1
                    total_syntax_error_score += corrupted_error_score[closes.index(c)]
        if len(tmp) > 0:
            incompletes += 1
            if prev_corrupted == corrupted:
                incomplete_lines.append(line)
    print(total_syntax_error_score)
    for line in incomplete_lines:
        tmp = []
        score = 0
        for c in line:
            if c in opens:
                tmp.append(c)
            if c in closes:
                t = tmp.pop()
        tmp.reverse()
        for t in tmp:
            score *= 5
            score += opens.index(t)+1
        incompletes_correction_scores.append(score)
    incompletes_correction_scores.sort()
    print(incompletes_correction_scores[int(len(incompletes_correction_scores)/2)])

if __name__ == '__main__':
    main()