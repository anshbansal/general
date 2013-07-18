import sys

def p():
    tests = int(next(sys.stdin))
    for test in xrange(tests):
        a = sum(map(lambda x: int(x[::-1]), next(sys.stdin).split()))
        print str(a)[::-1]
        
p()
