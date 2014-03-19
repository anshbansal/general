from itertools import count


def prob_025():
    a, b, digits = 1, 1, 1
    for number in count(2):
        if digits > 999:
            return number
        a, b = b, a + b
        digits = len(str(b))

if  __name__ == "__main__":
    print(prob_025())
