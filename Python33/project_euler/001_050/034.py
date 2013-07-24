#Took 9 seconds
#The limit of 2540161 is chosen becuause it is 7 * 9!
#Numbers higher than this give 7 digit-number which
#cannot be equal to 8 digit numbers
from math import factorial

def prob_034():
    facts = [factorial(i) for i in range(10)]
    ans = 0
    for i in range(10, 2540161):
        sums = 0
        temp = i
        while temp:
            sums += facts[temp % 10]
            temp //= 10

        if sums == i:
            ans += i

    return ans

if __name__ == "__main__":
    import time
    s = time.time()
    print(prob_034())
    print (time.time() - s)

