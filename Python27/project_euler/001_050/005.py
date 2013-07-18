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
        return (num1 * num2) / a


def prob_005():
    num = 1
    for i in xrange(1,21):
        num = lcm(num,i)
    return num

if __name__ == "__main__":
    print prob_005()
