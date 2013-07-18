from itertools import permutations as p

def q():
    pers = [i for i in p('0123456789')]

    ans = 0
    for c in pers[1000000 - 1]:
        ans *= 10
        ans += int(c)
    print ans

q()
