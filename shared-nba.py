with open('data.csv') as f:
    lines = [line.rstrip().split(",") for line in f.readlines()]

counts = {}
firsts = {}
lasts = {}
vorps = {}

for (first, last, vorp) in lines:

    if first in counts:
        counts[first] += 1
    else:
        counts[first] = 1
    if last in counts:
        counts[last] +=1
    else:
        counts[last] = 1

    if last in firsts:
        firsts[last] += [first]
    else:
        firsts[last] = [first]
    if first in lasts:
        lasts[first] += [last]
    else:
        lasts[first] = [last]

    full = "%s %s" % (first, last)
    if full in vorps:
        vorps[full].append(float(vorp))
    else:
        vorps[full] = [float(vorp)]

groups = []
for name in counts:
    if counts[name] >= 5:
        fulls = []
        if name in firsts:
            fulls += ["%s %s" % (first, name) for first in firsts[name]]
        if name in lasts:
            fulls += ["%s %s" % (name, last) for last in lasts[name]]
        fulls[0] = (fulls[0], 0)
        for i in range(1,len(fulls)):
            if fulls[i] == fulls[i-1][0]:
                fulls[i] = (fulls[i], fulls[i-1][1]+1)
            else:
                fulls[i] = (fulls[i], 0)
        fulls = sorted(fulls, key=lambda x: -vorps[x[0]][x[1]])[0:5]
        vorp = sum([vorps[full[0]][full[1]] for full in fulls])
        groups.append((vorp, [full[0] for full in fulls]))

def sorter(var):
    return (-var[0], var[1])

for group in sorted(groups, key=sorter):
    print("%d.1 %s, %s, %s, %s, %s" % (group[0], *group[1]))
