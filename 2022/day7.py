class directory:
    def __init__(self, p, subDir=[], files=[]) -> None:
        self.parent = p
        self.subDir = subDir
        self.files = files

def main():
    directories = []
    cwd = []
    with open("day7_input", 'r') as f:
        while True:
            line = f.readline().rstrip()
            if not line:
                break
            else:
                cmd = line.split('')
                print(cmd)

if __name__ == "__main__":
    main()