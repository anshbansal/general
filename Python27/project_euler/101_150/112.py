#Took 24 seconds
import time

def is_bouncy_num(num):
    lisst1 = [int(i) for i in str(num)]
    lisst2 = sorted(lisst1)
    if (lisst1 == lisst2) or (lisst1 == lisst2[::-1]):
        return False
    else:
        return True

def p():
    bouncy = 0.0
    non_bouncy = 0

    ratio = 0.1
    i = 1
    while ratio != 0.99:
        i += 1
        if is_bouncy_num(i):
            bouncy += 1.0
        else:
            non_bouncy += 1

        ratio = bouncy/i

    print "\n",i

s = time.time()
p()
print (time.time() - s)

