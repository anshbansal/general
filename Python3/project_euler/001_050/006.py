from sums import sum_linear_series, sum_of_squares


def prob_006():
    return sum_linear_series(100) ** 2 - sum_of_squares(100)

if __name__ == "__main__":
    print(prob_006())
