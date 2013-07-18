total = 0
for i in range(1,1001):
    cur = (i ** i)
    total += cur

total = str(total)
print total[len(total) - 10:]
