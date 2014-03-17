import math

def erat3(num, isprime = [3]):
    '''Returns list of Prime numbers

    Changes erat() function using methods of erat2() function

    Advantage:
    Half memory usage
    Takes 1/10th time if called in the same run for same or lower number
    Improvement in speed if it has been called before

    Disadvantage:
    Has storage between function calls - Takes up a lot of memory space'''
    #REQUIRES MATH MODULE
    if num < 2:
        return []
    
    if num > 2 * len(isprime) + 2:
        def mapping(i):
            return (i -3)/2

        first_new = 2 * len(isprime) + 3
        isprime += [num for num in xrange(first_new ,num + 1, 2)]
        
        temp2 = int(math.sqrt(num)) + 1
        for i in xrange(3,first_new, 2):
            if isprime[mapping(i)]:
                j = first_new//i
                if j == 1:
                    j = 3
                elif j % 2 == 0:
                    j += 1

                temp = j * i
                while temp <= num:
                    isprime[mapping(temp)] = 0
                    j += 2
                    temp = j * i
                    
        for i in xrange(first_new,temp2, 2):
            if isprime[mapping(i)]:
                j = 3
                temp = j * i
                while temp <= num:
                    isprime[mapping(temp)] = 0
                    j += 2
                    temp = j * i
    
    return [2] + filter(lambda x: x, isprime[:(num - 1)//2])


max_num = 50 * (10 ** 6)

max_num1 = int(pow(max_num, 1/2.0))
max_num2 = int(pow(max_num, 1/3.0))
max_num3 = int(pow(max_num, 1/4.0))

listt3 = [i ** 4 for i in erat3(max_num3)]
listt2 = [i ** 3 for i in erat3(max_num2)]
listt1 = [i ** 2 for i in erat3(max_num1)]

ans = set()
for i in listt1:
    for j in listt2:
        if i + j >= max_num:
            break

        for k in listt3:
            if i + j + k >= max_num:
                break

            ans.update([i + j + k])

print len(ans)
