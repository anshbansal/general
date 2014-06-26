__author__ = 'Aseem'

from collections import Counter


def sum_of_squares_of_digits(num):
    ans = 0
    while num > 0:
        ans += (num % 10) ** 2
        num //= 10
    return ans


def set_all(ends, members, value):
    for j in members:
        ends[j] = value


def prob_092():
    # TODO Maybe Optimize - 53.801 sec
    ends = [0] * 10000001
    for temp in range(1, 10000000):
        if ends[temp]:
            continue
        members = {temp}
        while (temp - 89) and (temp - 1):
            temp = sum_of_squares_of_digits(temp)
            members.add(temp)
            if ends[temp]:
                set_all(ends, members, ends[temp])
                break
        else:
            set_all(ends, members, temp)

    return Counter(ends)[89]


if __name__ == "__main__":
    from project_euler import common

    common.run_all(__name__)