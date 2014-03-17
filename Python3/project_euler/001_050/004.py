def prob_004():
    largest = 0
    for i in range(100, 1000):
        for j in range(i + 1 , 1000):
            num = i * j
            if num > largest and num == int(str(num)[::-1]):
                    largest = num
    return largest

if __name__ == "__main__":
    print(prob_004())
