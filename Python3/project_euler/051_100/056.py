from itertools import product

def prob_056():
    summ = 0
    for a, b in product(range(1,100), repeat = 2):
        cur = sum(int(i) for i in str(a ** b))
        if cur > summ:
            summ = cur
    return summ

if __name__ == "__main__":
    print(prob_056())
