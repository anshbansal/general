def prob_009():
    for c in xrange(1,997):
        for b in xrange(1,c):
            a = 1000 - b - c
            if (a < b) and (a > 0) and (a*a + b*b == c*c):
                return a * b * c

if __name__ == "__main__":
    print prob_009()
            
