def combinations(n, r):
    r = r if n - r > r else n - r
    ans = 1
    for i in range(1, r + 1):
        ans *= n + 1 - i
        ans //= i
    return ans

def prob_053():
    return sum(combinations(n, r) > 1000000
               for n in range(1, 101)
               for r in range(n + 1))

if __name__ == "__main__":
    print(prob_053())
