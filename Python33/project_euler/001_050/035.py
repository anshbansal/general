import math
def is_prime(num):
    temp = int(round(math.sqrt(num))) + 1
    for i in range(3,temp,2):
        if num % i == 0:
            return False
    return True

def circular_shift(num, shift):
    num = str(num)
    length = len(num)
    return int(num[length - shift:] + num [:length - shift])

def is_circular_prime(num, length):
    for i in str(num):
        if not(int(i) % 2):
            return False
    for check in range(length):
        if not is_prime(circular_shift(num, check + 1)):
            return False
    return True

def prob_035():
    return(4 + sum(is_circular_prime(i, len(str(i)))
                  for i in range(11,1000000,2)))

if __name__ == "__main__":
    print(prob_035())
