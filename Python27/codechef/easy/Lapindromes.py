import sys
def is_lapindrome(string,):
    if len(string) % 2:
        str1 = string[:len(string)/2]
        str2 = string[len(string)/2 + 1:]
    else:
        str1 = string[:len(string)/2]
        str2 = string[len(string)/2 :]

    freq1 = [0 for i in range(26)]
    freq2 = [0 for i in range(26)]

    for c in str1:
        freq1[ord(c) - ord('a')] += 1

    for c in str2:
        freq2[ord(c) - ord('a')] += 1

    for i in range(26):
        if freq1[i] != freq2[i]:
            return False

    return True

def p():
    nums = int(sys.stdin.readline())
    for i in range(nums):
        temp = raw_input()
        if is_lapindrome(temp):
            print "YES"
        else:
            print "NO"

p()
