def is_palindrome(num):
    if num == num[::-1]:
        return True
    return False

def prob_036():
    return sum(i for i in range(1,1000000)
               if is_palindrome(str(i)) and is_palindrome(bin(i)[2:]))

if __name__ == "__main__":
    print(prob_036())
