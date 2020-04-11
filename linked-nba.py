with open('data.csv') as f:
    lines = [line.rstrip().split(",") for line in f.readlines()]

firsts = {}
lasts = {}
vorps = {}

for (first, last, vorp) in lines:
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
        if float(vorp) > vorps[full]:
            vorps[full] = float(vorp)
    else:
        vorps[full] = float(vorp)

links = {}
for name in firsts:
    if name in lasts:
        links[name] = True

def extend_chains(chains):
    extended = []
    for chain in chains:
        next_first = chain[-1]
        for next_last in lasts[next_first]:
            if len(chain) == 4 or next_last in links:
                extended.append(chain + [next_last])
    if len(extended) == 0 or len(extended[0]) == 5:
        return extended
    else:
        return extend_chains(extended) 

scored = []
for name in links:
    chains = extend_chains([[name]])
    for chain in chains:
        for first in firsts[chain[0]]:
            name = "%s %s" % (first, chain[0])
            vorp = vorps[name]
            names = [name]
            for i in range(4):
                name = "%s %s" % (chain[i], chain[i+1])
                names.append(name)
                vorp += vorps[name]
            scored.append((vorp, names))

def sorter(var):
    return (-var[0], var[1])

for (vorp, names) in sorted(scored, key=sorter):
    print("%d.1 %s -> %s -> %s -> %s -> %s" % (vorp, *names))
