def prob_008():
    with open('008.txt') as f:
        number = ''
        for line in f:
            number += line[:-1]

    largest = 0
    for i in range(995):
        product = 1
        for j in range(5):
            product *= int(number[i + j])
        if product > largest:
            largest = product
    return largest

if __name__ == "__main__":
    print(prob_008())