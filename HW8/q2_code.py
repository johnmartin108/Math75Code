#necessary constants
ZZnZZ = Integers(1021)
h = 228
g = 10
m = int(sqrt(1021)) + 1

BS = []
GS = []

#compute lists
for i in range(m):
    BS.append(ZZnZZ(h)*ZZnZZ(g**i))
    GS.append(ZZnZZ(g)**((i+1)*m))
    
#technically, we should sort the lists, but that makes it hard to keep track of what
#exponent generated which element, which is an interesting speed/memory tradeoff. I 
#just naively compared the lists.
for j in range(m):
    for k in range(m):
        if BS[j] == GS[k]:
            print ((k+1)*m-j)

#check answer
print ZZnZZ(10)**481