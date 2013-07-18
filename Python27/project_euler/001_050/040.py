s = ''

i = 1
while len(s) < 1000000:
    s += str(i)
    i += 1

total = 1
for i in xrange(7):
    total *= int(s[10 ** i - 1])

print total
