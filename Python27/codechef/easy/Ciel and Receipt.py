import sys
def p():
    cases = int(sys.stdin.readline())
    for case in xrange(cases):
        num = int(sys.stdin.readline())
        temp = 2048
        menus = 0

        while num > 0:
            while (num - temp) >= 0:
                num -= temp
                menus += 1

            temp /= 2
            if temp == 0:
                temp = 1

        print menus

p()
        
