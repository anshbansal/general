__author__ = 'Aseem'

import primes


def prob_087():
    max_num = 50 * (10 ** 6)

    max_num1 = int(pow(max_num, 1/2))
    max_num2 = int(pow(max_num, 1/3))
    max_num3 = int(pow(max_num, 1/4))

    listt3 = [i ** 4 for i in primes.primes_list_mem(max_num3)]
    listt2 = [i ** 3 for i in primes.primes_list_mem(max_num2)]
    listt1 = [i ** 2 for i in primes.primes_list_mem(max_num1)]

    ans = set()
    for i in listt1:
        for j in listt2:
            if i + j >= max_num:
                break

            for k in listt3:
                if i + j + k >= max_num:
                    break

                ans.update([i + j + k])
    return len(ans)

if __name__ == "__main__":
    print(prob_087())