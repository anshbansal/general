def combinations(n, r):
    r = r if n - r > r else n - r
    ans = 1
    for i in range(1, r + 1):
        ans *= n + 1 - i
        ans //= i
    return ans

def prob_015():
    return combinations(40, 20)

if __name__ == "__main__":
    print(prob_015())
