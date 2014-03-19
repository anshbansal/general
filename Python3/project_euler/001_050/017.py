NUMS = {
    0 : 0, #This value makes one condition less
    1 : 3, 2 : 3, 3 : 5, 4 : 4, 5 : 4, 6 : 3, 7 : 5, 8 : 5, 9 : 4,
    10 : 3, 11 : 6, 12 : 6, 13 : 8, 14 : 8, 15 : 7, 16 : 7, 17 : 9,
    18 : 8, 19 : 8
    }


def numeral_to_string(num):
    ans = 0
    if num > 999:
        ans += len("onethousand")
        num %= 1000

    if num > 99:
        temp = num//100
        ans += NUMS[temp]
        if num % 100:
            ans += len("hundredand")
        else:
            ans += len("hundred")
            
        num %= 100

    if num > 19:
        #Strings of 80 and 90 have same length
        #Strings of 40, 50, 60 have same length
        #Strings of 20, 30 have same length
        if num > 79:
            ans += 6
        elif num > 69:
            ans += 7
        elif num > 39:
            ans += 5
        else:
            ans += 6
        num %= 10

    #NUMS[num] for num < 20
    return (ans + NUMS[num])


def prob_017():
    return sum(numeral_to_string(i) for i in range(1,1001))

if __name__ == "__main__":
    print(prob_017())
