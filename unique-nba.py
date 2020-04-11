with open('data.csv') as f:
    lines = [line.rstrip().split(",") for line in f.readlines()]

counts = {}

for (first, last, unused) in lines:
    if first in counts:
        counts[first] += 1
    else:
        counts[first] = 1
    if last in counts:
        counts[last] +=1
    else:
        counts[last] = 1

unique = []
for (first, last, vorp) in lines:
    if counts[first] == 1 and counts[last] == 1:
        unique.append((vorp, first, last))

def sorter(var):
    return (-float(var[0]), var[1], var[2])

for name in sorted(unique, key=sorter):
    print("%s %s %s" % name)
