def one_to_ten(temp):
    ans =''
    if temp == 1:
        ans += "one"
    elif temp == 2:
        ans += "two"
    elif temp == 3:
        ans += "three"
    elif temp == 4:
        ans += "four"
    elif temp == 5:
        ans += "five"
    elif temp == 6:
        ans += "six"
    elif temp == 7:
        ans += "seven"
    elif temp == 8:
        ans += "eight"
    else:
        ans += "nine"
    return ans
    

def numeral_to_string(num):
    ans = ""
    if num > 999:
        ans += "onethousand"
        num %= 1000

    if num > 99:
        temp = num/100
        ans += one_to_ten(temp)
        if num % 100 == 0:
            ans += "hundred"
        else:
            ans += "hundredand"
        num %= 100

    if num > 19:
        if num > 89:
            ans += "ninety"
        elif num > 79:
            ans += "eighty"
        elif num > 69:
            ans += "seventy"
        elif num > 59:
            ans += "sixty"
        elif num > 49:
            ans += "fifty"
        elif num > 39:
            ans += "forty"
        elif num > 29:
            ans += "thirty"
        else:
            ans += "twenty"
        num %= 10

    if num > 9:
        if num == 10:
            ans += "ten"
        elif num == 11:
            ans += "eleven"
        elif num == 12:
            ans += "twelve"
        elif num == 13:
            ans += "thirteen"
        elif num == 14:
            ans += "fourteen"
        elif num == 15:
            ans += "fifteen"
        elif num == 16:
            ans += "sixteen"
        elif num == 17:
            ans += "seventeen"
        elif num == 18:
            ans += "eighteen"
        else:
            ans += "nineteen"

        return ans

    if num > 0:
        ans += one_to_ten(num)

    return ans

def p():
    total  = 0
    for i in xrange(1,1001):
        total += len(numeral_to_string(i))
    print total

p()
