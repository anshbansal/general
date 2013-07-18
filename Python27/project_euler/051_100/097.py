def p():
    cur = 28433
    cur = cur * pow(2, 7830457, 10 ** 10)
    cur %= 10 ** 10

    cur += 1
    print cur

p()
