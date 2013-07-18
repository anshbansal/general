num = '''75
95 64
17 47 82
18 35 87 10
20 04 82 47 65
19 01 23 75 03 34
88 02 77 73 07 63 67
99 65 04 28 06 16 70 92
41 41 26 56 83 40 80 70 33
41 48 72 33 47 32 37 16 94 29
53 71 44 65 25 43 91 52 97 51 14
70 11 33 28 77 73 17 78 39 68 17 57
91 71 52 38 17 14 91 43 58 50 27 29 48
63 66 04 68 89 53 67 30 73 16 69 87 40 31
04 62 98 27 23 09 70 98 73 93 38 53 60 04 23'''
num = num.split('\n')
num = [i.split(' ') for i in num]
num = [[int(j) for j in i] for i in num]

i = 0
listt1 = []
listt1.append(num[i][0])

while i < len(num):
    
    listt2 = []
    i += 1

    if i >= len(num):
        print max(listt1)
        break
    
    cur_row_length = len(num[i])

    for j in xrange(cur_row_length):
        total = num[i][j]

        if j == 0:
            total += listt1[j]
        elif j == cur_row_length - 1:
            total += listt1[j - 1]
        else:
            if listt1[j-1] > listt1[j]:
                total += listt1[j-1]
            else:
                total += listt1[j]
        listt2.append(total)

    #print listt2

    listt1 = []
    i += 1

    if i >= len(num):
        print max(listt2)
        break
    
    cur_row_length = len(num[i])

    for j in xrange(cur_row_length):
        total = num[i][j]

        if j == 0:
            total += listt2[j]
        elif j == cur_row_length - 1:
            total += listt2[j - 1]
        else:
            if listt2[j-1] > listt2[j]:
                total += listt2[j-1]
            else:
                total += listt2[j]
        listt1.append(total)

    #print listt1
