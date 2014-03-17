from itertools import count

def is_bouncy_num(num):
    lisst1 = [int(i) for i in str(num)]
    lisst2 = sorted(lisst1)
    if (lisst1 == lisst2) or (lisst1 == lisst2[::-1]):
        return False
    return True

def prob_112():
    bouncy = 0
    for i in count(2):
        if is_bouncy_num(i):
            bouncy += 1

        if bouncy/i == 0.99:
            return i

if __name__ == "__main__":
    print(prob_112())
