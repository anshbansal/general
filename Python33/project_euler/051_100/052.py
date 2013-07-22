from itertools import count

def prob_052():
    for num in count(1):
        for j in range(2, 7):
            if set(str(j * num)) != set(str(num)):
                break
        else:
            return num

if __name__ == "__main__":
    print(prob_052())
