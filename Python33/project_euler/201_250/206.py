#Taking 22 seconds
import math
import time

def prob_206():
    #num1 = int(math.sqrt(10203040506070809))
    num2 = int(math.sqrt(19293949596979899))
    #print(num1, num2)
    
    for num1 in [101010103, 101010107]:
    # 3*3 = 9, 7*7 = 49
    #Hence num1 has these 2 values
        for i in range(num1, num2 + 1, 10):
            sq = str(i ** 2)
            for k in range(7, -1, -1):
                if int(sq[2 * k]) - (k + 1):
                    break
            else:
                return i * 10

if __name__ == "__main__":
    s = time.time()
    print(prob_206())
    print (time.time() - s)
