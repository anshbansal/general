import sys

def p():
    tests = int(next(sys.stdin))
    for test in range(tests):
        a = sum(map(lambda x: int(x[::-1]), next(sys.stdin).split()))
        while a % 10 == 0:
            a //= 10
        print(str(a)[::-1])
        
p()
