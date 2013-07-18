def prob_003(num):
    '''Returns the largest prime factor of a number'''
    i = 3
    while i <= num:
        if num % i:
            pass
        else:
            ans = i
            num /= i
            while True:
                if num % i:
                    break
                else:
                    num /= i

        i += 2

    return ans

if __name__ == "__main__":
    print prob_003(600851475143)
