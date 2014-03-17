#To understand how this works just make a (4,4) matrix
#Then follow the steps. Easy to understand that way.
SIZE = 80
def prob_081():
    with open('081.txt') as f:
        mat = [[int(i) for i in line[:-1].split(',')]
               for line in f]
    
    for i in range(1, SIZE):
        for j in range(i + 1):
            if j == 0:
                mat[i][j] += mat[i -1][j]
                mat[j][i] += mat[j][i - 1]
            else:
                mat[i][j] += mat[i][j - 1] if mat[i -1][j] > mat[i][j - 1] \
                             else mat[i -1][j]

                if i != j:
                    mat[j][i] += mat[j - 1][i] if mat[j][i -1] > mat[j - 1][i] \
                                 else mat[j][i -1]

    return mat[SIZE - 1][SIZE - 1]

if __name__ == "__main__":
    print(prob_081())
