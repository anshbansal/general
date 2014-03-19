import math


def is_triangle_num(n):
    temp = (-1 + math.sqrt(8 * n + 1))/2
    if temp == int(temp):
        return True
    return False


def prob_042():
    with open('Resources\\042.txt') as f:
        words = f.readline().split(',')

    triangles = 0
    for word in words:
        value = sum((ord(c) - ord('A') + 1)
                    for c in word[1:-1])
        if is_triangle_num(value):
            triangles += 1

    return triangles

if __name__ == "__main__":
    print(prob_042())
