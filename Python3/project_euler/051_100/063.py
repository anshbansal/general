from itertools import count

def prob_063():
    ans = set()
    prev_len = 0
    for i in count(1):
        for j in count(1):
            temp = i ** j
            if len(str(temp)) != j:
                break
            ans.update([i**j])
            
        if len(ans) == prev_len:
            return prev_len
        prev_len = len(ans)

if __name__ == "__main__":
    print(prob_063())
