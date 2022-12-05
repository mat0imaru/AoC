f = open("day1.txt","r")

num_elf = 1

most_calories_elf = 0
most_calories = 0
tot_calories = 0
tot_cal_list = []
print(f"elf number {num_elf}")
while 1:
    line = f.readline()
    if not line:
        break
    if line == "\n":
        if most_calories < tot_calories:
            most_calories = tot_calories
            most_calories_elf = num_elf
        print(f"total_calories = {tot_calories}")
        num_elf += 1
        tot_cal_list.append(tot_calories)
        tot_calories = 0
        print(f"elf number {num_elf}")
    else:
        cal = int(line.rstrip())
        tot_calories += cal
        print(cal)

print(f"most calories elf = {most_calories_elf}")
print(f"most calories = {most_calories}")
tot_cal_list.sort()
tot_cal_list.reverse()
print(tot_cal_list)
print(tot_cal_list[0]+tot_cal_list[1]+tot_cal_list[2])