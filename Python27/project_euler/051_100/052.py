def int_to_list_of_int(num):
    num = str(num)
    num = [int(i) for i in num]
    return num

def contain_same_digits(lisst1, lisst2):
    if len(lisst1) != len(lisst2):
        return False

    for c in lisst1:
        if c not in lisst2:
            return False

    return True

not_found = True

num_int = 0
while not_found:
    num_int += 1

    num = num_int
    
    num2 = str(2 * num)
    if len(str(num)) != len(num2):
        continue

    num3 = str(3 * num)
    if len(str(num)) != len(num3):
        continue

    num4 = str(4 * num)
    if len(str(num)) != len(num4):
        continue

    num5 = str(5 * num)
    if len(str(num)) != len(num5):
        continue

    num6 = str(6 * num)
    if len(str(num)) != len(num6):
        continue

    num  = set(str(num))
    num2  = set(num2)
    num3  = set(num3)
    num4  = set(num4)
    num5  = set(num5)
    num6  = set(num6)

    if num == num2 and num == num3 and num == num4 and num == num5 and num == num6:
        not_found = False

print num_int
