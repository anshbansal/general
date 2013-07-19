def sum_of_series(num):
    return (num * (num + 1))/2

def prob_001(num):
    '''Returns sum of multiples of 3 or 5 below num'''
    num -= 1
    ans  = 3 * sum_of_series(num//3)
    ans += 5 * sum_of_series(num//5)
    ans -= 15 * sum_of_series(num//15)
    return int(ans)

if __name__ == "__main__":
    print(prob_001(1000))
