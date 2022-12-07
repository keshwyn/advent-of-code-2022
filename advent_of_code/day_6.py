with open('./advent_of_code/day6_input', 'r') as f:
#with open('./advent_of_code/day6_test_data', 'r') as f:
    contents = f.readlines() 

buffer = contents[0]

i = 0
signal = []

for character in buffer:
    if len(signal) == 14:
        print(i)
        break

    i += 1
    if character in signal:
        pos = signal.index(character) + 1
        signal = signal[pos:]
        signal.append(character)
    else:
        signal.append(character)

