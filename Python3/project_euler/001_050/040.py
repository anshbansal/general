from itertools import count

def prob_040():
    s = ''
    for i in count(1):
        s += str(i)
        if len(s) >= 1000000:
            break

    total = 1
    for i in range(7):
        total *= int(s[10 ** i - 1])

    return total

if __name__ == "__main__":
    print(prob_040())
