def reverse_num(num):
    rev = 0
    while num > 0:
        rev *= 10
        rev += num % 10
        num /= 10
    return rev

def prob_004():
    largest = 0
    for i in xrange(100, 1000):
        for j in xrange (i + 1 , 1000):
            num = i * j
            if num > largest and num == reverse_num(num):
                    largest = num
    return largest

if __name__ == "__main__":
    print prob_004()
