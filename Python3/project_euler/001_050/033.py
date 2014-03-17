from fractions import Fraction as f
from itertools import product

def prob_033():
    ans = f(1,1)
    for num, den in product(range(10,100), repeat = 2):
        if num >= den:
            continue

        num_list = [i for i in str(num)]
        den_list = [i for i in str(den)]
        temp = [i for i in num_list if i in den_list]

        if len(temp) is not 1 or '0' in temp:
            continue

        num_list.remove(temp[0])
        den_list.remove(temp[0])

        num2 = int(num_list[0])
        den2 = int(den_list[0])

        if not(num2 and den2):
            continue
        
        if f(num,den) == f(num2,den2):
            ans *= f(num,den)

    return ans

if __name__ == "__main__":
    print(prob_033())
