import math

def prob_099():
    try:
        with open('099.txt') as f:
            largest = 0
            i = 0
            for line in f:
                i += 1
                a, b = map(int, line.split(','))
                current = b * math.log(a)
                if current > largest:
                    largest = current
                    print(i)
    except:
        pass

if __name__ == "__main__":
    prob_099()
