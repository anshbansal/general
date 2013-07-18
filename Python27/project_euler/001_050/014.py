#Taking 56 seconds
import time

def next_num(num):
    if num % 2:
        return 3 * num + 1
    else:
        return num/2

def collatz(num):
    current = 0
    while num != 1:
        num = next_num(num)
        current += 1
    return current

def p():
    longest = 1
    longest_num = 1
    for i in xrange(1, 1000000):
        current = collatz(i)
        if current > longest:
            longest = current
            longest_num = i
    print longest_num, "produces sequence of length = ", longest


s = time.time()
p()
print (time.time() - s)
