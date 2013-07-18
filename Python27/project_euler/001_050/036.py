def decimal_to_other(num,base):
    '''Converts from decimal to other number system'''
    add = num % base
    if num <= 1:
        return str(num)
    else:
        return str(decimal_to_other(num//base,base)) + str(add)

def is_palindrome(num):
    '''checks whether a number is palindrome or not'''
    if str(num) != str(num)[::-1]:
        return False
    else:
        return True

total  = 0
for i in xrange(1,1000000):
    if is_palindrome(i) and is_palindrome(decimal_to_other(i,2)):
        total += i
print total
