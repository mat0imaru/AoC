class directory:
    parent = []
    subDir = []
    files = []
    
    def totalSize(self):
        tot = 0
        for f in self.files:
            tot += f.size
        return tot

class file:
    def __init__(self, nm, sz):
        self.name = nm
        self.size = sz
    def __repr__(self) -> str:
        return f"{self.name} size of {self.size}"

def main():
    filtered = {}
    directories = {}
    cwd = []
    with open("day7_input", 'r') as f:
        while True:
            line = f.readline().rstrip()
            if not line:
                break
            else:
                cmd = line.split(' ')
                # print(cmd)
                if cmd[0] == '$':
                    # print("input")
                    if cmd[1] == "cd":
                        # print("change directory")
                        if cmd[2] == "..":
                            cwd.pop()
                            # print(f"cwd: {'/'.join(cwd).replace('//','/')}")
                        elif cmd[2] == ".":
                            # print(f"cwd: {'/'.join(cwd).replace('//','/')}")
                            pass
                        else:
                            cwd.append(cmd[2])
                            # print(f"cwd: {'/'.join(cwd).replace('//','/')}")
                            if not '/'.join(cwd).replace('//','/') in directories:
                                directories['/'.join(cwd).replace('//','/')] = []
                    elif cmd[1] == "ls":
                        pass
                        # print("list")
                    else:
                        print("Error: wrong command")
                else:
                    # print("output")
                    if cmd[0] == 'dir':
                        # print("directory")
                        pass
                    else:
                        # print("file")
                        directories['/'.join(cwd).replace('//','/')].append(file(cmd[1],int(cmd[0])))
    # print(directories)
    simplified = {}
    for dir in directories:
        # print(f"cwd:{dir}")
        tot = 0
        for cursor in directories:
            if dir == cursor[0:len(dir)]:
                # print(f"----{cursor}")
                # print(f"files: {directories[cursor]}")
                for f in directories[cursor]:
                    tot += f.size
        # print(f"total size: {tot}")
        simplified[dir] = tot
        if tot < 100000:
            filtered[dir] = tot
        if tot > 3956976:
            print(f"cwd:{dir}")
            print(f"total size: {tot}")
    ans = 0
    for fit in filtered:
        # print(f"{fit} size of {filtered[fit]}")
        ans += filtered[fit]
    print(ans)
    print(f"total used space = {simplified['/']}")
    using = 70000000 - simplified['/']
    print(f"space need  free = {30000000 - using}")

if __name__ == "__main__":
    main()

exit()

{'/': 43956976,
 '/dtcfhsm': 19406820, 
 '/dtcfhsm/drjhjtm': 3669401, 
 '/dtcfhsm/drjhjtm/cvrf': 1544596, 
 '/dtcfhsm/drjhjtm/cvrf/tpwvvbh': 870980, 
 '/dtcfhsm/drjhjtm/cvrf/tpwvvbh/sdwjz': 269696, 
 '/dtcfhsm/drjhjtm/cvrf/tpwvvbh/vrgjhvrd': 67409, 
 '/dtcfhsm/drjhjtm/cvrf/tpwvvbh/wqcsrw': 178435, 
 '/dtcfhsm/drjhjtm/cvrf/tpwvvbh/wqcsrw/ttgwphbc': 178435, 
 '/dtcfhsm/drjhjtm/gddqh': 717536, 
 '/dtcfhsm/drjhjtm/gddqh/cfvpq': 322334, 
 '/dtcfhsm/drjhjtm/gddqh/cfvpq/ljncp': 146594, 
 '/dtcfhsm/drjhjtm/gddqh/wwv': 76789, 
 '/dtcfhsm/drjhjtm/gddqh/wwv/zqzch': 76789, 
 '/dtcfhsm/drjhjtm/gddqh/wwv/zqzch/jllhmmf': 76789, 
 '/dtcfhsm/drjhjtm/gddqh/wwv/zqzch/jllhmmf/pvqhg': 76789, 
 '/dtcfhsm/drjhjtm/qccmn': 524791, 
 '/dtcfhsm/drjhjtm/qccmn/czpnrsfc': 401174, 
 '/dtcfhsm/drjhjtm/qccmn/czpnrsfc/tdwmpl': 84395, 
 '/dtcfhsm/drjhjtm/qjgv': 574721, 
 '/dtcfhsm/drjhjtm/sjgwv': 307757, 
 '/dtcfhsm/hjlmf': 313069, 
 '/dtcfhsm/jllhmmf': 327426, 
 '/hblzj/qlg/vfsj/ndsfzz/jllhmmf/mjzcf': 561469, 
 '/hblzj/qlg/vfsj/ndsfzz/jllhmmf/vmjjtbl': 426021, 
 '/hblzj/qlg/vfsj/ndsfzz/jllhmmf/vmjjtbl/sjqpfc': 426021, 
 '/hblzj/qlg/vfsj/ndsfzz/jllhmmf/vmjjtbl/sjqpfc/mbpfvsg': 128515, 
 '/hblzj/qlg/vfsj/ndsfzz/jllhmmf/vmjjtbl/sjqpfc/vfwvtscb': 297506, 
 '/hblzj/qlg/vfsj/ndsfzz/jllhmmf/vmjjtbl/sjqpfc/vfwvtscb/ljv': 297506, 
 '/hblzj/qlg/vfsj/ndsfzz/jllhmmf/vmjjtbl/sjqpfc/vfwvtscb/ljv/nwbfd': 297506, 
 '/hblzj/qlg/vfsj/ndsfzz/vdfmwrq': 36060, 
 '/hblzj/qlg/vfsj/ndsfzz/vdfmwrq/ntm': 36060, 
 '/hblzj/qlg/vfsj/ndsfzz/zwzlr': 126975, 
 '/hblzj/qlg/vfsj/rsqhz': 1632953, 
 '/hblzj/qlg/vfsj/rsqhz/cjzh': 105519, 
 '/hblzj/qlg/vfsj/rsqhz/dsssbm': 611421, 
 '/hblzj/qlg/vfsj/rsqhz/dsssbm/frmmlzv': 165168, 
 '/hblzj/qlg/vfsj/tsmlpnbc': 877846, 
 '/hblzj/qlg/vfsj/tsmlpnbc/bdb': 100286, 
 '/hblzj/qlg/vfsj/tsmlpnbc/ddjd': 261837, 
 '/hblzj/qlg/vfsj/tsmlpnbc/ddjd/vmwddb': 261837, 
 '/hblzj/qlg/vfsj/tsmlpnbc/gbdm': 233279, 
 '/hblzj/qlg/vfsj/tsmlpnbc/grm': 8883, 
 '/hblzj/qlg/vfsj/tsmlpnbc/grm/cghd': 8883, 
 '/hblzj/qlg/vfsj/zmljzwt': 3979145, 
 '/hblzj/qlg/vfsj/zmljzwt/ltpmzrtf': 222040, 
 '/hblzj/qlg/vfsj/zmljzwt/qtwnndbg': 877928, 
 '/hblzj/qlg/vfsj/zmljzwt/qtwnndbg/ltgqs': 45032, 
 '/hblzj/qlg/vfsj/zmljzwt/qtwnndbg/nqngjr': 296145, 
 '/hblzj/qlg/vfsj/zmljzwt/shfjtm': 2604356, 
 '/hblzj/qlg/vfsj/zmljzwt/shfjtm/dqv': 327447, 
 '/hblzj/qlg/vfsj/zmljzwt/shfjtm/jhgdb': 1215026, 
 '/hblzj/qlg/vfsj/zmljzwt/shfjtm/jhgdb/nfd': 654120, 
 '/hblzj/qlg/vfsj/zmljzwt/shfjtm/jhgdb/nfd/tdslfhgq': 654120, 
 '/hblzj/qlg/vfsj/zmljzwt/shfjtm/jhgdb/nfd/tdslfhgq/jnfrd': 475956, 
 '/hblzj/qlg/vfsj/zmljzwt/shfjtm/jhgdb/qwng': 202921, 
 '/hblzj/qlg/vfsj/zmljzwt/shfjtm/jhgdb/zwdbl': 219865, 
 '/hblzj/qlg/vfsj/zmljzwt/shfjtm/jllhmmf': 258183, 
 '/hblzj/qlg/vfsj/zmljzwt/shfjtm/sczqst': 37030, 
 '/hblzj/qlg/vfsj/zmljzwt/shfjtm/zngqfcw': 766670, 
 '/hblzj/qlg/vfsj/zmljzwt/shfjtm/zngqfcw/fmwlfgm': 512148, 
 '/hblzj/qlg/wqcsrw': 111251, 
 '/hblzj/rsgbjpp': 5750480, 
 '/hblzj/rsgbjpp/dchrnhrl': 925301, 
 '/hblzj/rsgbjpp/dchrnhrl/gqznj': 276324, 
 '/hblzj/rsgbjpp/lsqztz': 290574, 
 '/hblzj/rsgbjpp/lsqztz/cmrqhlf': 290574, 
 '/hblzj/rsgbjpp/lwlh': 3692446, 
 '/hblzj/rsgbjpp/lwlh/flc': 162731, 
 '/hblzj/rsgbjpp/lwlh/pjm': 2042591, 
 '/hblzj/rsgbjpp/lwlh/pjm/bzctws': 89520, 
 '/hblzj/rsgbjpp/lwlh/pjm/ljv': 210757, 
 '/hblzj/rsgbjpp/lwlh/pjm/vjjhgjmp': 1285542, 
 '/hblzj/rsgbjpp/lwlh/pjm/vjjhgjmp/ljv': 137884, 
 '/hblzj/rsgbjpp/lwlh/pjm/vjjhgjmp/qvpcmscg': 360496, 
 '/hblzj/rsgbjpp/lwlh/pjm/vjjhgjmp/rsbdmvjq': 296157, 
 '/hblzj/rsgbjpp/lwlh/pjm/vjjhgjmp/wqcsrw': 271684, 
 '/hblzj/rsgbjpp/lwlh/pjm/vjjhgjmp/wqcsrw/ljv': 271684, 
 '/hblzj/rsgbjpp/lwlh/pjm/vjjhgjmp/wqcsrw/ljv/mrw': 271684, 
 '/hblzj/rsgbjpp/lwlh/vhs': 869310, 
 '/hblzj/rsgbjpp/lwlh/vhs/hsjs': 551831, 
 '/hblzj/rsgbjpp/lwlh/vhs/jhvqqcls': 145011, 
 '/hblzj/rsgbjpp/lwlh/vhs/jhvqqcls/wqcsrw': 145011, 
 '/hblzj/rsgbjpp/lwlh/zqwvr': 477557, 
 '/hblzj/rsgbjpp/slb': 842159, 
 '/hblzj/tpjpnjg': 37762, 
 '/hblzj/vmwddb': 2532312, 
 '/hblzj/vmwddb/ctgzpnn': 1991338, 
 '/hblzj/vmwddb/ctgzpnn/jbfqtvhl': 110122, 
 '/hblzj/vmwddb/ctgzpnn/shnnqff': 1175419, 
 '/hblzj/vmwddb/ctgzpnn/shnnqff/srbf': 142423, 
 '/hblzj/vmwddb/ctgzpnn/shnnqff/srbf/fqhhcdcm': 142423, 
 '/hblzj/vmwddb/ctgzpnn/shnnqff/vmwddb': 738555, 
 '/hblzj/vmwddb/ctgzpnn/shnnqff/vmwddb/jllhmmf': 238385, 
 '/hblzj/vmwddb/ctgzpnn/shnnqff/vmwddb/ljv': 380291, 
 '/hblzj/vmwddb/lwvcw': 115763, 
 '/hblzj/vmwddb/wpw': 187278, 
 '/jbssdwf': 31839, 
 '/ljv': 270886, 
 '/nhp': 76321, 
 '/nhp/sgffh': 76321}