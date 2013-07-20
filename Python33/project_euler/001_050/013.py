def prob_013():
    try:
        with open('013.txt') as f:
            total = 0
            for line in f:
                total += int(line)
            return str(total)[:10]
    except:
        return 0

if __name__== "__main__":
    print(prob_013())
