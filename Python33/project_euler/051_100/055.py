def is_palindrome(num):
    if num != num[::-1]:
        return False
    return True

def prob_055():
    total = 0
    for num in range(1,10000):
        count = 0
        temp = num
        while count < 50:
            temp += int(str(temp)[::-1])
            if is_palindrome(str(temp)):
                break
            count += 1
        else:
            total += 1

    return total

if __name__ == "__main__":
    print(prob_055())
            
