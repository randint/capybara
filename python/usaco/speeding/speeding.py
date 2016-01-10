f = open("2.in", 'r')
n = int(f.readline().split()[0])
seg, bseg = [], []

for line in f:
    values = line.split()
    pair = int(values[0]), int(values[1])
    if len(seg) < n:
        if len(seg) == 0:
            seg.append(pair)
        else:
            seg.append((pair[0] + seg[-1][0], pair[1]))
    else:
        if len(bseg) == 0:
            bseg.append(pair)
        else:
            bseg.append((pair[0] + bseg[-1][0], pair[1]))

print n
print seg
print bseg

for d in range(100):
    pass
