from collections import Counter
from operator import itemgetter

counters = [Counter() for _ in range(8)]
with open("input.txt") as input_file:
    for line in input_file:
        for index, char in enumerate(line.strip()):
            counters[index].update([char])
            
signal = "".join(map(itemgetter(0), [x.most_common(1)[0] for x in counters]))
            
print("Part one:", signal)

signal = "".join(map(itemgetter(0), [x.most_common()[-1] for x in counters]))

print("Part two:", signal)
