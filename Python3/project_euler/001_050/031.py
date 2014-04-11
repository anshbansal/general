__author__ = 'Aseem'


def prob_031():
    range_value = [(3, 100), ()]
    #TODO Took 1.407 seconds
    ways = 1
    for i in range(3): #For 100
        sum_ = i * 100
        for j in range(5): #for 50
            sum_a = sum_ + j*50
            if sum_a > 200:
                break
            for k in range(11): #For 20
                sum_b = sum_a + k*20
                if sum_b > 200:
                    break
                for l in range(21): #For 10
                    sum_c = sum_b + l*10
                    if sum_c > 200:
                        break
                    for m in range(41): #For 5
                        sum_d = sum_c + m*5
                        if sum_d > 200:
                            break
                        for n in range(101): #for 2
                            sum_e = sum_d + n*2
                            if sum_e > 200:
                                break
                            for o in range(201): #For 1
                                if sum_e + o == 200:
                                    ways += 1

    return ways

import time
s = time.time()
print(prob_031())
print(time.time() - s)
