def prob_002(num):
    #TODO Maybe refactor
    """Returns the sum of even fibonnaci numbers below num"""
    a, b = 1, 2
    total = 0
    while b < num:
        if b % 2 == 0:
            total += b
        a, b = b, a + b

    return total

if __name__ == "__main__":
    print(prob_002(4000000))
