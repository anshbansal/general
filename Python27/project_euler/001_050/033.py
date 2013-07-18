from fractions import Fraction as f

ans = f(1,1)
for num in xrange(10,100):
    for den in xrange(10,100):
        if num >= den:
            continue

        num_list = [i for i in str(num)]
        den_list = [i for i in str(den)]

        temp = []
        for i in num_list:
            if i in den_list:
                temp.append(i)

        if len(temp) != 1 or temp[0] == '0':
            continue

        num_list.remove(temp[0])
        den_list.remove(temp[0])

        num2 = int(num_list[0])
        den2 = int(den_list[0])

        if num2 == 0 or den2 == 0:
            continue

        if f(num,den) == f(num2,den2):
            ans *= f(num,den)

print ans
