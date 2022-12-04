# Read in the file
# Iterate through the file, doing math
#   If you throw X, score 1;
#   if you throw Y, score 2;
#   if you throw Z, score 3;
# Print math results


with open('./advent_of_code/day2_input', 'r') as f:
    contents = f.readlines() 

sum = 0
for line in contents:
    l = line.strip()
    points = 0
    split_l = l.split()
    if split_l[1] == 'X':
        points += 0
    elif split_l[1] == 'Y':
        points += 3
    elif split_l[1] == 'Z':
        points += 6

    if split_l[1] == 'X':
        if split_l[0] == 'A':
            points += 3
        if split_l[0] == 'B':
            points += 1
        if split_l[0] == 'C':
            points += 2
    elif split_l[1] == 'Y':
        if split_l[0] == 'A':
            points += 1
        if split_l[0] == 'B':
            points += 2
        if split_l[0] == 'C':
            points += 3
    elif split_l[1] == 'Z':
        if split_l [0] == 'A':
            points += 2
        if split_l [0] == 'B':
            points += 3
        if split_l[0] == 'C':
            points +=1


    print(points)
    sum += points

print(sum)