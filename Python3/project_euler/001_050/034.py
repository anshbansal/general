#The limit of 2540161 is chosen because it is 7 * 9!
#See 2540162 It is seven digits but for factorial's value
#to increase the number of digits will have to be 8
from math import factorial


def prob_034():
    #TODO May be Optimized - 5.219 sec
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
    print(time.time() - s)