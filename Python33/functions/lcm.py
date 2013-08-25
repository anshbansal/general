def lcm(num1, num2):
    '''Finding LCM of a number '''
    '''Uses Euclid's algorithm for finding GCD'''
    if num1 == 0 or num2 == 0:
        return 0

    if num1 >= num2:
        a = num1
        b = num2
    else:
        a = num2
        b = num1

    while b != 0:
        c = a % b
        a,b = b,c
    else:
        return (num1 * num2) // a

def lcm2(num1, num2):
    '''Finding LCM of a number '''
    '''Uses Euclid's algorithm for finding GCD'''
    if not(num1 and num2):
        return 0

    a, b = (num1, num2) if num1 >= num2 else (num2, num1)
    while b:
        a, b = b, a % b
    return (num1 * num2) // a
