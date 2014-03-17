#To do this I derived the formula for sum of corners in n x n spiral
#It's easy to find the pattern if you consider the outer ring only in spiral

def sum_of_outer_ring(n):
    return 4*(n*n) - 6 * (n - 1)

def prob_028():
    return 1 + sum(sum_of_outer_ring(i)
                   for i in range(3, 1002, 2))

if __name__ == "__main__":
    print(prob_028())


