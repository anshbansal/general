import sys

def p():
    tests = int(next(sys.stdin))
    for i in xrange(tests):
        stri = next(sys.stdin)
        count = 2
        for j in xrange(1, len(stri) - 1):
            if ord(stri[j]) < ord(stri[j-1]):
                count += 27 + ord(stri[j]) - ord(stri[j-1])
            else:
                count += 1 + ord(stri[j]) - ord(stri[j-1])

        if count <= (len(stri) - 1) * 11:
            print "YES"
        else:
            print "NO"

p()

