__author__ = 'Aseem'


def prob_031():
    #TODO Optimize Took 1.407 seconds
    ways = 1
    for i in range(3):
        sum_a = i * 100
        for j in range(5):
            sum_b = sum_a + j*50
            if sum_b > 200:
                break
            for k in range(11):
                sum_c = sum_b + k*20
                if sum_c > 200:
                    break
                for l in range(21):
                    sum_d = sum_c + l*10
                    if sum_d > 200:
                        break
                    for m in range(41):
                        sum_e = sum_d + m*5
                        if sum_e > 200:
                            break
                        for n in range(101):
                            sum_f = sum_e + n*2
                            if sum_f > 200:
                                break
                            for o in range(201):
                                if sum_f + o == 200:
                                    ways += 1

    return ways

import time
s = time.time()
print(prob_031())
print(time.time() - s)
