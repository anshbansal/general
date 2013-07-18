def p():
    a, b = 1,1
    digits = 1
    number = 2
    while digits < 1000:
        a,b = b, a+b
        digits = len(str(b))
        number += 1
    return number

print p()
