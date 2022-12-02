
# Input file contains numeric data of calories, one entry per line.
# A blank line indicates an end of the elf
# Summing up the lines before the blank line gives the total calories for that elf

# while line:
#   if line is blank, conclude elf
#   elsif file is end, conclude elf
#   else add value to current elf
# 
# sort through caloric values of elf, find greatest value


with open('./day_1/input', 'r') as f:
    contents = f.readlines() 

elf = 0
elves = [0]

for line in contents:
    l = line.strip()
    if l == '':
        elf += 1
        elves.append(0)
    else:
        elves[elf] += int(l)

highest = 0
for an_elf in elves:
    if an_elf > highest:
        highest = an_elf

print(highest)