SMALLPRIMES = [2,3,5,7,11,13,17,19,23]
LSP = len(SMALLPRIMES)
ndiv = lambda d, n: n % d != 0
all_true = lambda a, b: a and b
def isprime(n):

    if n < 2 or type(n) != type(2):
        return False
    if n in SMALLPRIMES:
        return True
    nn = [n for i in range(LSP)]
    if not reduce(all_true, map(ndiv, SMALLPRIMES, nn), True):
        return False
    sn = n ** 0.5
    S = 24
    while S + 5 < sn:
        for i in [1,5]:
            if not ndiv(S+i, n):
                return False
        S += 6
    return True

import unittest
class PrimeWorks(unittest.TestCase):
    def testPrimes(self):
        self.assertTrue( isprime(2) )
        self.assertTrue( isprime(3) )
        self.assertFalse( isprime(4) )
        self.assertTrue( isprime(101) )
        self.assertFalse( isprime(899) )

def tryInserting(n, k):
    if type(n) == type(0):
        return tryInserting_(n, k)
    else:
        return [tryInserting_(i,k) for i in n]
        
def tryInserting_( n, k ):
    # we know n is prime.
    # can we insert a digit at position k that keeps it a prime?
    s = str(n)
    poss = [int( "%s%d%s" % (s[:k-1], i, s[k-1:])) for i in range(10) ]
    ok = filter( isprime, poss )
    return ok
        
### CANDIDATEPRIMES
### xx[x]xxxxxxxxxxx (14 digits) 3
### [x]xxxxxxxxxxxx (13 digits)  1
### xxx[x]xxxxxxxx (12 digits)   4
### [x]xxxxxxxxxx (11 digits)    1
### xxxx[x]xxxxx (10 digits)     5
### xxxxxxxx[x] (9 digits)
### x[x]xxxxxx (8 digits)
### xxxxx[x]x (7 digits)
### xxxx[x]x (6 digits)
### xx[x]xx (5 digits)

### Generate a four-digit prime number
n = 1002
out = []
while n < 10002:
    for i in [1,5]:
        if isprime(n+i):
            # try inserting
            ok1 = tryInserting( n+i, 3 )
            ok2 = reduce(lambda a, b: a+b, tryInserting( ok1, 5), [])            
            ok3 = reduce(lambda a, b: a+b, tryInserting( ok2, 6), [])
            ok4 = reduce(lambda a, b: a+b, tryInserting(ok3, 2), [])
            ok5 = reduce(lambda a, b: a+b, tryInserting(ok4, 9), [])
            ok6 = reduce(lambda a, b: a+b, tryInserting(ok5, 5), [])
            ok7 = reduce(lambda a, b: a+b, tryInserting(ok6, 1), [])
            ok8 = reduce(lambda a, b: a+b, tryInserting(ok7, 4), [])
            ok9 = reduce(lambda a, b: a+b, tryInserting(ok8, 1), [])
            ok = reduce(lambda a, b: a+b, tryInserting(ok6, 3), [])
            print n+i, ok
            out += ok
    n += 6
        
unittest.main()
    
