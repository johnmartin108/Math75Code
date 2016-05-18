#witness-testing function
def test_witness(n,w):
    if w % n == 0:
        return false
    
    n1 = n-1

    #check congruences until we hit a^u, pulling out 2s from n-1 as we go
    while int(n1/2) == n1/2:
        if ZZnZZ(w)**n1 == ZZnZZ(-1):
            return false
        n1 = n1/2
    
    #final congruency check - is a^u congruent to 1?
    if ZZnZZ(w)**n1 == 1:
        return false
    return true

#plug in numbers from the problem
ns = [1009, 2009]
ZZnZZ = Integers(n)
witnesses = [3,5,7,11,13]
for n in ns:
    for w in witnesses:
        if test_witness(n,w):
            print str(w) + " is a witness for the compositeness of " + str(n)
        else:
            print str(w) + " is not a witness for the compositeness of " + str(n)