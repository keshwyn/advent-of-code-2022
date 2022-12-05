import re

with open('./advent_of_code/day5_input', 'r') as f:
    contents = f.readlines() 

initializing = True

# Find how many stacks we have
stacks = []
for line in contents:
    l = line.strip()
    if l == '':
        break
    if l.startswith('1'):
        split_l = l.split()
        for number in split_l:
            temp_stack = [number]
            stacks.append(temp_stack)
length = len(stacks)

# Get the stacks into useful lists.
for line in contents:
    l = line.replace(']\n','];')
    if l.startswith(' 1'):
        break

    l = l.replace('] ', '];')
    l = l.replace('    ', '[*];')
    l = l.strip('\n')

    l_list = l.split(';')
    i = 0
    while i < len(stacks):
        if (l_list[i] != '[*]' and l_list[i] != '   '):
            temp_string = l_list[i].replace('[','')
            temp_string = temp_string.replace(']','')
            stacks[i].insert(0, temp_string)
        i += 1

for list in stacks:
    list.pop()
#print(stacks)


# OK, now we can start handling the 
for line in contents:
    if line.startswith('move'):

        #print(line)
        l = line.split()
        move = int(l[1])
        start = int(l[3]) - 1 
        dest = int(l[5]) - 1

        i = 0
        temp_list = []
        while i < move:
            temp_list.append(stacks[start].pop())
            i += 1
        stacks[dest].extend(temp_list)

        #print(stacks)

for list in stacks:
    print(list[-1], sep='', end='')
    
