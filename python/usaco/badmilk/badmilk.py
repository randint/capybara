'''
D: drinks, 1-1000
N: people, 1-N
M: milks, 1-50
T: time, 1-100
'''

f = open("badmilk.in", 'r')
line = f.readline().split()
N, M, D, S = int(line[0]), int(line[1]), int(line[2]), int(line[3])
print N, M, D, S

people = [[] for i in range(N)] # list of size N of empty lists
for i in range(D):
    global people
    line = f.readline().split()
    p, m, t = int(line[0]), int(line[1]), int(line[2])
    people[p-1].append((m, t))

sick = [False] * N
for i in range(S):
    line = f.readline().split()
    p, t = int(line[0]), int(line[1])
    sick[p-1] = t

for p in people:
    print p

print sick

suspects = [i for i in range(1, M + 1)]
print suspects

for i, p in enumerate(sick):
    if p != False: # if sick
        for s in suspects:
            # if people[i] did not drink milk s before time p, remove s from suspects 
            drankSuspect = False
            for drinks in people[i]:
                if drinks[0] == s and drinks[1] < p:
                    drankSuspect = True
            if drankSuspect == False:
                suspects.remove(s)

print suspects

# list.index(value)

dosesNeeded = 0
for s in suspects:
    possible = 0
    for i in range(N):
        drankSuspect = False
        for drinks in people[i]:
            if drinks[0] == s:
                drankSuspect = True
        if drankSuspect:
            possible += 1
    if possible > dosesNeeded:
        dosesNeeded = possible

print dosesNeeded

f.close()

# write to file badmilk.out
out = open("badmilk.out", 'w')
out.write(str(dosesNeeded))
out.close()
