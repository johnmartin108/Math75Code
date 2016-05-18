def generator_func(x):
    return x^2+1

def pollard_rho(n):
    
    ZZnZZ = Integers(n)

    #seed value of 2
    rand_vals = [2]
    
    #generate plenty of random values, just to be save - we computed
    #in class that we need 2sqrt(n) values, I think
    for i in range(0, int(sqrt(2*n))):
        next_val = ZZnZZ(generator_func(rand_vals[i]))
        rand_vals.append(next_val)
    
    #loop over all possible cycle lengths
    for i in range(1, len(rand_vals)/2):

        #the expression inside the parentheses is computed modulo n
        test = int(rand_vals[2*i] - rand_vals[i])
        if test == 0 or test == 1:
            continue

        #just taking the gcd assumes we already know factors of n
        #compromise trying to divide n by all the factors of test. Is this cheating?
        #Can we assume we know the factors of test?
        for f in list(factor(test)):
            if n % f[0] == 0:

                #recurse! this should make it return a list of prime factors ultimately
                #calling the function recursively twice because the factor we
                #stumbled upon is not necessarily prime
                return pollard_rho(f[0]) + ", " + pollard_rho(n/f[0])
    
    return str(n)

print pollard_rho(53477)