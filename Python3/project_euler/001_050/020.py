def factorial(num):
    ans = 1
    while num > 1:
        ans *= num
        num -= 1
    return ans


def prob_020():
    return sum(int(i) for i in str(factorial(100)))

if __name__ == "__main__":
    print(prob_020())
