def lcm(num1, num2):
    '''Finding LCM of a number '''
    '''Uses Euclid's algorithm for finding GCD'''
    if not(num1 and num2):
        return 0

    a, b = (num1, num2) if num1 >= num2 \
           else (num2, num1)
    while b:
        a, b = b, a % b
    return (num1 * num2) // a


def prob_005():
    num = 1
    for i in range(1,21):
        num = lcm(num,i)
    return num

if __name__ == "__main__":
    print(prob_005())
