


with open('./advent_of_code/day3_input', 'r') as f:
    contents = f.readlines() 

priority = 0
part = 'B'

dict = {'a':1}
i = 1
for letter in range(ord('b'), ord('z')+1):
    i += 1
    dict[chr(letter)] = i
for letter in range(ord('A'), ord('Z')+1):
    i += 1
    dict[chr(letter)] = i

line_a = ''
line_b = ''
line_c = ''
count = 0

for line in contents:
    if part == 'A':
        list_line = list(line.strip())
        size = len(line.strip())//2

        # OK, let's get the unique values from each half
        first_half = list(set(sorted(list_line[0:size])))
        second_half = list(set(sorted(list_line[-size:])))

        bad_thing = '.'
        for e in first_half:
            if e in second_half:
                bad_thing = e
                break
    
        #print(bad_thing, ":", dict[bad_thing])
        priority += dict[bad_thing]
    else:
        list_line = list(line.strip())
        count += 1
        if count == 1:
            line_a = list(set(sorted(list_line)))
        elif count == 2:
            line_b = list(set(sorted(list_line)))
        elif count == 3:
            line_c = list(set(sorted(list_line)))
            count = 0
            for e in line_c:
                if (e in line_a and e in line_b):
                    print("Shared token:", e)
                    priority += dict[e]
                    break
            
print(priority)