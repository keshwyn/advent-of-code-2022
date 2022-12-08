with open('./advent_of_code/day7_input', 'r') as f:
#with open('./advent_of_code/day7_test_data', 'r') as f:
    contents = f.readlines() 

directories = ['/']
depth = 0
x = ' '
parent = ['/']
dirlist = []
filelist = []

debug = False

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
                else:
                    depth += 1
                    parent.append(command[2])
                    dirlist.append(command[2])
                    if debug:
                        print(("{} - {} (dir)").format(x*(((depth)*2)-1), command[2]))
    elif l.startswith('dir'):
        # This is a directory inside of the ls
        # We can ignore empty directories (for now, that may come up) so we're going to skip these lines.
        dir = l.split()
        dirlist.append(dir[1])
    else:
        f = l.split()
        if debug:
            print("{} - {} (file, size={}) (parent={})".format(x*(((depth+1)*2)-1), f[1], f[0], parent))
        p = parent[:] # lists aren't immutable, so I have to do this to make sure the parent doesn't get overwritten.
        filelist.append([f[1], f[0], p])

smalldirs = 0
dirlist = sorted(set(dirlist))
for dir in dirlist:
    print(dir)       
    i = 0
    for file in filelist:
        if dir in file[2]:
            i += int(file[1])
    if debug:
        print(dir, i)

    if i < 100000:
        print(dir, i)
        smalldirs += i

i = 0
for file in filelist:
    i += int(file[1])
if i < 100000:
    print("/", i)

print(smalldirs)