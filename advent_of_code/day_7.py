#with open('./advent_of_code/day7_input', 'r') as f:
with open('./advent_of_code/day7_test_data', 'r') as f:
    contents = f.readlines() 

directories = ['/']
depth = 0
x = ' '
parent = ['/']

debug = True

for line in contents:
    l = line.strip('\n')
    if l.startswith('$'):
        listing = False
        # OK, we've either got an ls or a cd; we're into command sections, not pos
        command = l.split()
        if command[1] == 'ls':
            listing = True # the next lines in the file are directory or filenames, until we hit another $
        else:
            if command[1] == 'cd':
                if command[2] == '/':
                    depth = 0
                    parent = ['/']
                    if debug:
                        print('- / (dir)')
                elif command[2] == '..':
                    depth -= 1
                    parent.pop()
                    # parent == parent of current directory - have to look that up
                else:
                    depth += 1
                    parent.append(command[2])
                    if debug:
                        print(("{} - {} (dir)").format(x*(((depth)*2)-1), command[2]))

    elif l.startswith('dir'):
        # This is a directory inside of the ls
        # We can ignore empty directories (for now, that may come up) so we're going to skip these lines.
        next
    else:
        f = l.split()
        if debug:
            print("{} - {} (file, size={}) (parent={})".format(x*(((depth+1)*2)-1), f[1], f[0], parent))
