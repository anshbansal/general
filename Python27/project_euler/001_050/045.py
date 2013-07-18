from math import sqrt

i = 286
a = False
b = False
while not a  or not b:
    tri_num = (i * (i + 1)) /2

    p = (1 + sqrt(1 + 24 * tri_num))//6

    a = False
    if (p * (3 * p - 1))/2 == tri_num:
        a = True

    h = (1 + sqrt(1 + 8 * tri_num))//4

    b = False
    if a and ((h *(2 * h - 1)) == tri_num):
        b = True
        print "Pent = ",p
        print "Hex = ",h

    i += 1

print "\n", i, tri_num
