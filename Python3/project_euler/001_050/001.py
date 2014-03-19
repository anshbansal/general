from sums import sum_linear_series


def prob_001(num):
    #TODO Change logic to get reusable component
    num -= 1
    ans = 3 * sum_linear_series(num//3)
    ans += 5 * sum_linear_series(num//5)
    ans -= 15 * sum_linear_series(num//15)
    return int(ans)

if __name__ == "__main__":
    print(prob_001(1000))