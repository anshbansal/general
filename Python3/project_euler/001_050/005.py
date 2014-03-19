from lcm import lcm


def prob_005():
    num = 1
    for i in range(1, 21):
        num = lcm(num, i)
    return num

if __name__ == "__main__":
    print(prob_005())
