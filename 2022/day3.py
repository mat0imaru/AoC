
priorities = {
    'a':1, 'b':2, 'c':3, 'd':4, 'e':5, 'f':6,
    'g':7, 'h':8, 'i':9, 'j':10,'k':11,'l':12,
    'm':13,'n':14,'o':15,'p':16,'q':17,'r':18,
    's':19,'t':20,'u':21,'v':22,'w':23,'x':24,
    'y':25,'z':26,'A':27,'B':28,'C':29,'D':30,
    'E':31,'F':32,'G':33,'H':34,'I':35,'J':36,
    'K':37,'L':38,'M':39,'N':40,'O':41,'P':42,
    'Q':43,'R':44,'S':45,'T':46,'U':47,'V':48,
    'W':49,'X':50,'Y':51,'Z':52 }

def main():
    SoP = 0
    # f = open("day3_input_sample", 'r')
    f = open("day3_input", 'r')
    # errors = []
    lines = []
    while True:
        line = f.readline().strip()
        lines.append(line)
        if not line:
            break
        compartments = [line[:len(line)//2], line[len(line)//2:]]
        # print(compartments)
        compartmentA = set()
        compartmentB = set()
        error = ''
        for c in compartments[0]:
            compartmentA.add(c)
        for c in compartments[1]:
            compartmentB.add(c)
        error = list(compartmentA&compartmentB)[0]
        # print(error)
        SoP += priorities[error]
        # errors.append(error)
    # print(errors)
    print(SoP)
    SoP = 0
    for i in range(int(len(lines)/3)):
        # print(lines[i*3])
        # print(lines[i*3+1])
        # print(lines[i*3+2])
        A = set()
        for item in lines[i*3]:
            A.add(item)
        B = set()
        for item in lines[i*3+1]:
            B.add(item)
        C = set()
        for item in lines[i*3+2]:
            C.add(item)
        SoP += priorities[list(A&B&C)[0]]
    print(SoP)

if __name__ == "__main__":
    main()