def rev_pos(num):
    return int(str(num)[::-1])

def prob_004():
    largest = 0
    for i in range(100, 1000):
        for j in range(i + 1 , 1000):
            num = i * j
            if num > largest and num == rev_pos(num):
                    largest = num
    return largest

if __name__ == "__main__":
    print(prob_004())
