__author__ = 'Aseem'

from collections import Counter


def sum_of_squares_of_digits(num):
    ans = 0
    while num > 0:
        ans += (num % 10) ** 2
        num //= 10
    return ans


def prob_092():
    #TODO Maybe Optimize - 56.984 sec
    ends = [0] * 10000001
    for i in range(1, 10000000):
        members = set([i])
        q = members.update
        temp = i
        while not ends[temp] and (temp - 89) and (temp - 1):
            temp = sum_of_squares_of_digits(temp)
            q([temp])

        if ends[temp]:
            for i in members:
                ends[i] = ends[temp]
        else:
            for i in members:
                ends[i] = temp

    return Counter(ends)

if __name__ == "__main__":
    import time
    t = time.time()
    print(prob_092())
    print(time.time() - t)