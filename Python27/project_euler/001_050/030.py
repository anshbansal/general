sums = 0
for i in xrange(10, 354295):
    sums_of_pow = 0
    temp = i
    while temp > 0:
        sums_of_pow += pow(temp % 10,5)
        temp = temp / 10

    if sums_of_pow == i:
        sums += i

print "Sum =",sums
