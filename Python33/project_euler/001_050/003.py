def prob_003(num):
    '''Returns the largest prime factor of an odd number'''
    i = 3
    while i <= num:
        if num % i:
            pass
        else:
            ans = i
            while True:
                num //= i
                if num % i:
                    break
        i += 2

    return ans

if __name__ == "__main__":
    print(prob_003(600851475143))
