def prob_016():
    num = str(2 ** 1000)
    return sum(int(i) for i in num)

if __name__ == "__main__":
    print(prob_016())
