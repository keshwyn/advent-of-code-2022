with open('./advent_of_code/day4_input', 'r') as f:
    contents = f.readlines() 

def integers(a, b):
    return list(range(a,b+1))

subset_count = 0
disjoint_count = 0
for line in contents:
    l = line.strip()
    split_l = l.split(',')
    pair_1 = split_l[0].split('-')
    pair_2 = split_l[1].split('-')

    set_1 = set((integers(int(pair_1[0]), int(pair_1[1]))))
    set_2 = set((integers(int(pair_2[0]), int(pair_2[1]))))

    if (set_1.issubset(set_2) or set_2.issubset(set_1)):
        subset_count += 1
    
    if (not set_1.isdisjoint(set_2)):
        disjoint_count += 1

print("Subsets:", subset_count)
print("Overlaps:", disjoint_count)