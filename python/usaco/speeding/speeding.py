f = open("2.in", 'r')
n = int(f.readline().split()[0])
seg, bseg = [], []
for line in f:
    data = line.split()
    pair = int(data[0]), int(data[1])
    if len(seg) < n:
        seg.append(pair)
    else:
        bseg.append(pair)
'''
print n
print seg
print bseg
'''
for d in range(100):
    pass
