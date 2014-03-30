__author__ = 'Aseem'


def prob_030():
    sums = 0
    for i in range(10, 354295):
        sums_of_pow = 0
        temp = i
        while temp > 0:
            sums_of_pow += pow(temp % 10, 5)
            temp //= 10

        if sums_of_pow == i:
            sums += i
    return sums

if __name__ == "__main__":
    print(prob_030())