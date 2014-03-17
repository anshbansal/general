def prob_022():
    with open('022.txt') as f:
        names = f.readline().split(',')
        names.sort()

    scores = 0
    for i in range(len(names)):
        score = 0
        for c in names[i][1:-1]:
            score += ord(c) - ord('A') + 1
        scores += (score * (i + 1))
    return scores

if __name__ == "__main__":
    print(prob_022())
