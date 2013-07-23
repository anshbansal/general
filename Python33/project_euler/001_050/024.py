from itertools import permutations as p

def prob_024():
    j = 0
    for i in p('0123456789'):
        j += 1
        if j == 1000000:
            j = 0
            for c in i:
                j *= 10
                j += int(c)
            return j

if __name__ == "__main__":
    print(prob_024())
