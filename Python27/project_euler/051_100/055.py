def is_palindrome(num):
    '''checks whether a number is palindrome or not'''
    if str(num) != str(num)[::-1]:
        return False
    else:
        return True

def p():
    total = 0
    for num in xrange(1,10000):
        count = 0
        temp = num
        while count < 50:
            temp += int(str(temp)[::-1])
            if is_palindrome(temp):
                break
            else:
                count += 1
        else:
            total += 1

    print total

p()
            
