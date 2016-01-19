#print 3 + 5

#x = 3
#y = 5

#print x + y

#for i in range(1,11):
#    print i, i**2

start = 960000
end = 960000

n_with_most = 1
most_results = 0

for n in range(start, end + 1):
    print "---------" + str(n) + "---------"
    results = 0
    for i in range(1, n/2+2):
        x = (n + i*i) / (2.0*i)
        if x % 1.0 == 0 and i < x:
            print int(x), int(x - i)
            results += 1
        if results > most_results:
            n_with_most = n
            most_results = results

print "%d: %d results" %(n_with_most, most_results)
