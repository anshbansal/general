def sum_of_series(num):
    return (num * (num + 1))//2

def sum_of_squares(num):
    return (num * (num + 1) * (2 * num + 1))//6

def prob_006():
    return sum_of_series(100) ** 2 - sum_of_squares(100)

if __name__ == "__main__":
    print(prob_006())
