def prob_067():
    with open('067.txt') as f:
        mat = [[int(i) for i in line[:-1].split(' ')]
                  for line in f]
    for row_num in range(1, len(mat)):
        pre = mat[row_num - 1]
        cur = mat[row_num]

        for el_num in range(len(cur)):
            total = cur[el_num]
            if el_num == 0:
                total += pre[el_num]
            elif el_num == len(cur) - 1:
                total += pre[el_num - 1]
            else:
                total += pre[el_num - 1] if pre[el_num - 1] > pre[el_num] \
                         else pre[el_num]

            mat[row_num][el_num] = total
    return max(mat[len(mat) - 1])

if __name__ == "__main__":
    print(prob_067())
