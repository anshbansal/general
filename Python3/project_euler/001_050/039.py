def prob_039():
    maximum = 0
    maximum_p = 3
    for p in range(3, 1001):
        cur = 0
        for a in range(1, p-1):
            #This equation can be obtained by solving the two given equations
            b = (p * (p - 2 * a))/(2.0 * (p - a))
            if b != int(b):
                continue
            c = p - a - b
            if c <= 0:
                break
            if a*a + b*b == c*c:
                cur += 1
        if cur > maximum:
            maximum = cur
            maximum_p = p
    return maximum_p

if __name__ == "__main__":
    print(prob_039())
