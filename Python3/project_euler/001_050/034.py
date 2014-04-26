from math import factorial


def prob_034():
    facts = [factorial(i) for i in range(10)]
    ans = 0
    limit = factorial(9) * 7
    for num in range(10, limit):
        temp_num = num
        sums = 0
        while temp_num:
            sums += facts[temp_num % 10]
            temp_num //= 10

        if sums == num:
            ans += num

    return ans

if __name__ == "__main__":
    import time
    s = time.time()
    print(prob_034())
    print(time.time() - s)